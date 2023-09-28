$( document ).ready(function() {
  showstar();
});

function showstar(){
    z=0
    
    const elems=document.getElementsByClassName("ratings")
    var elemslength = elems.length;
    
    for (var elm = 0; elm < elemslength; elm++){
        var rating=parseFloat(elems[elm].getAttribute("id"))/2;
        
        var child=elems[elm].children;
        
        for (var childelm = 0; childelm < rating; childelm+=1){
            
            if (childelm==rating-0.5){
                child[childelm].querySelector('svg').insertAdjacentHTML("beforeend",'<path d="M288 0c-12.2 .1-23.3 7-28.6 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3L288 439.8V0zM429.9 512c1.1 .1 2.1 .1 3.2 0h-3.2z" fill="orange"/>')
            }
            else{
                child[childelm].setAttribute("style", "fill:orange;");
            };
        };
     
    }
    Array.from(elems).forEach(b=>b.removeAttribute('class'));
    
};
var step = 1;
var loading = false;
function getDocumentHeight() {
    return Math.max(
        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
    );
    }
$(window).on("scroll.once", function() {
    setTimeout(async () => {

            var docHeight = getDocumentHeight();
            if(loading === false){
    if ($(window).scrollTop() + window.innerHeight >= docHeight-5){

            loading = true;
            const url = new URL(window.location);
            page=url.searchParams.get("page");
            if (page==null){
                page=1;
            };
            let c =parseInt(page)+1;
            st=url.searchParams.get("q");
            $.ajax({
                
                type: 'GET',
                url: "ajaxlisting",
                data: {"cpage": c,"searchtext":st},
                success: function (response) {
    
    
    
                    for (var key in response) {
                        for (var i = 0; i < response[key].length; i++) {
                            var pname = response[key][i].productname;
                            var price = response[key][i].productprice;
                            var image = response[key][i].productimage;
                            var rating = response[key][i].productrating;
                            var ratingcount = response[key][i].productratingcount;
                            var slug = response[key][i].slug;
                            inhtml=   '<div class="col p-2 p-lg-3">    <div class="card border border-1 shadow-sm" id="prdcard" style="">' +
                            '<div class="bg-image hover-zoom ripple ripple-surface ripple-surface-light text-center" data-mdb-ripple-color="light">' +
                            '<img id="cardphoto" src="media/'+image+'" class="w-100" style="object-fit: contain;aspect-ratio: 1 / 1;"/><a href="#!">'+
                            '<div class="hover-overlay"><div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div></div></a></div><div class="card-body p-2 mt-0 align-middle" >'+
                            '<a href="/urunler/'+slug+'" class="text-reset" style="text-decoration: none;">'+
                            '<span id="cardname" class="card-title display-3 mx-0 px-0 mb-2" style="height:32px;" >'+pname+'</span></a><div class="d-flex justify-content-between align-items-center">'+
                            '<div id="'+rating+'" class="ratings">'+
                                    '<i style="fill:#e4e4e4"><svg height="1em" viewBox="0 0 576 512"><path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"/></svg></i>'+  
                                    '<i style="fill:#e4e4e4"><svg height="1em" viewBox="0 0 576 512"><path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"/></svg></i>'+
                                    '<i style="fill:#e4e4e4"><svg height="1em" viewBox="0 0 576 512"><path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"/></svg></i>'+
                                    '<i style="fill:#e4e4e4"><svg height="1em" viewBox="0 0 576 512"><path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"/></svg></i>'+
                                    '<i style="fill:#e4e4e4"><svg height="1em" viewBox="0 0 576 512"><path d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"/></svg></i>'+
                                    '<span class="mb-0 px-0 py-0 my-0 text-body-secondary" style="font-size:12px !important ">('+ratingcount+')</span>'+
                                    '</div>'+ 
                                    '</div>'+
                                    '<div class="text-center mb-1" style="">'+
                                    '<hr class="mb-3 mt-1">'+
                                    '<span class="mb-1" style="font-size:14px ; font-weight:600 !important;" id="cardprice">'+price+' TL</span></div></div>'+
                                    
                                    '<button id="addbtn" type="button" class="btn w-100  rounded-bottom" style="font-weight:400 !important;height:40px" data-mdb-ripple-color="dark">Sepete Ekle</button>'+
                                    '</div>'+
                                    '</div>';
                        
                
                            document.getElementById('listdiv').insertAdjacentHTML("beforeend",inhtml);

    
                             
                                     }
                        
                        };
                        
                        if (response["object"].length == 0) {
                            return
                        }
                        showstar()
                        let c =parseInt(page)+1;
                       
                        url.searchParams.set('page',c);
                        history.replaceState(null, null, url);
                        loading = false;

                        

    
                },
                error: function (response) {
                    console.log(response)
                }
            })
        }

    };
}, 300);

});

