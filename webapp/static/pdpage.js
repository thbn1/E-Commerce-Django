
$.ajax({
    
    type: 'GET',
    url: "pdpage/",
    data: {"cpage": c,"searchtext":st},
    success: function (response) {

        for (var key in response) {
         
            }
    //succes code

            


    },
    error: function (response) {
        console.log(response)
    }
})