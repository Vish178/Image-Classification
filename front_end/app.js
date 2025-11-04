Dropzone.autoDiscover = false;

function init() {
    let dz = new Dropzone("#dropzone", {
        url: "/",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    });
    
    dz.on("addedfile", function() {
        if (dz.files[1]!=null) {
            dz.removeFile(dz.files[0]);        
        }
    });

    dz.on("complete", function (file) {
        let imageData = file.dataURL;
        
        var url = "http://127.0.0.1:5000/predict";

        $.post(url, {
            image_data: file.dataURL
        },function(data, status) {
            // Find celebrity with highest confidence
            if (!data || Object.keys(data).length === 0) {
                $("#resultHolder").hide();
                $("#divClassTable").hide();
                $("#bestCelebrityHolder").hide();
                $("#error").show();
                return;
            }
            let bestCelebrity = null;
            let bestScore = -Infinity;
            for (let name in data) {
                if (data[name] > bestScore) {
                    bestScore = data[name];
                    bestCelebrity = name;
                }
            }
            // Show large image and name
            let card = $(`[data-player='${bestCelebrity}']`).html();
            $("#bestCelebrityHolder").html(`<div style='max-width:350px;margin:auto;'>${card}</div><h2 style='margin-top:20px;'>${bestCelebrity} <span style='font-size:1rem;'>(Confidence: ${bestScore.toFixed(2)})</span></h2>`);
            $("#bestCelebrityHolder").show();
            // dz.removeFile(file);
        });
    });

    $("#submitBtn").on('click', function (e) {
        dz.processQueue();		
    });
}

$(document).ready(function() {
    console.log( "ready!" );
    $("#error").hide();
    $("#resultHolder").hide();
    $("#divClassTable").hide();

    init();
});