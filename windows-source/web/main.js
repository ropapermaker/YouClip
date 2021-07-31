var proccessRunning = false;

function startProcess() {

    if (proccessRunning == false){
        proccessRunning = true;

        // Get all user input
        var videoUrl = document.getElementById("url").value;
        var startMin = document.getElementById("startmin").value;
        var startSec = document.getElementById("startsec").value;
        var endMin = document.getElementById("endmin").value;
        var endSec = document.getElementById("endsec").value;


        // Get check fields
        var check1 = document.getElementById("chk1txt");
        var check1conf = document.getElementById("chk1cnfrm");

        var check2 = document.getElementById("chk2txt");
        var check2conf = document.getElementById("chk2cnfrm");

        var check3 = document.getElementById("chk3txt");
        var check3conf = document.getElementById("chk3cnfrm");

        var finalconf = document.getElementById("finalcnfrm");

        check1.style.display = "none";
        check1conf.style.display = "none";

        check2.style.display = "none";
        check2conf.style.display = "none";

        check3.style.display = "none";
        check3conf.style.display = "none";

        finalconf.style.display = "none";
        // Execute python function to check if link is valid
        var result = eel.check_video_url(videoUrl)();

        // Display the Field Saying "Checking Link"
        check1.style.display = "block";


        result.then(res => {

            if (res=="valid"){
                check1conf.textContent = "Video Link is Valid.";
                check1conf.style.display = "block";


                // Display the Field Saying "Downloading Video"
                check2.style.display = "block";

                // Call python function to download the video
                var download = eel.download_video(videoUrl)();

                // Checks if download was successful and gives output
                download.then(res =>{
                    if (res=="downloaded") {
                        check2conf.textContent = "Download Successful.";
                        check2conf.style.display = "block";

                        check3.style.display = "block";

                        var crop = eel.crop_video(startMin, startSec, endMin, endSec)();

                        crop.then(res => {
                            if (res == "fail"){
                                check3conf.textContent = "Cropping Failed.";
                            } else if (res == "greater60") {
                                check3conf.textContent = " Some Values Are Greater Than 60.";

                            } else if (res == "greaterstart") {
                                check3conf.textContent = "Start Is Longer Than End Time.";
                            } else if (res == "equal") {
                                check3conf.textContent = "Start And End Time Are Equal.";
                            } else if (res == "empty") {
                                check3conf.textContent = "Time Fields Are Empty.";
                            } else if (res == "less"){
                                check3conf.textContent = "You Need To Give Atleast 2 Time Values!";
                            } else {
                                check3conf.textContent = "Video Cropped Successfully."
                                var a = "Video Successfully Saved In Your Desktop With Name: ";
                                var b = res
                                var c = a + b
                                finalconf.textContent = c;
                            }

                            check3conf.style.display = "block";
                            finalconf.style.display = "block";

                        })

                    } else if (res=="error") {
                        check2conf.textContent = "Download Not Successful.";
                        check2conf.style.display = "block";
                    }


                }).catch(err => {
                })

            } else if (res=="invalid") {
                check1conf.textContent = "Video Does Not Exist.";
                check1conf.style.display = "block";
            } else if (res=="schema"){
               check1conf.textContent = "Make Sure The Link Starts With `https://`.";
               check1conf.style.display = "block";

            } else if (res=="notyt") {
                check1conf.textContent = "That Is Not A Youtube Link.";
                check1conf.style.display = "block";
            } else if (res=="unknownerror") {
                check1conf.textContent = "An Unknown Error Happened.";
                check1conf.style.display = "block";
            }

        }).catch(err => {
        })

    proccessRunning = false;
    } else {
        console.log("A process is currently running...");
    }
}
