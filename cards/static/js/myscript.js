
    
$( document ).ajaxStart(function() {
      show_loading();
});
    
    
$(document).ajaxStop(function(){
        hide_loading();
});
    
    
function show_toast(title,body,status){
          $("#toast_header").html(title);
          $("#toast_body").html(body);
          if(status == 'succses')
          $("#box_toast").css("background-color","lightgreen");
          if(status == 'error')
          $("#box_toast").css("background-color","salmon");

          $("#box_toast").toast("show");
} 

function show_loading(){
      $("#gif_loading").show();
}

function hide_loading(){
      $("#gif_loading").hide();
}


//save group ajax 
$("#groupform").submit(function(e) {
      
            e.preventDefault(); // avoid to execute the actual submit of the form.
      
            var form = $(this);
            var url = form.attr('action');
    
            $.ajax({
                  type: "POST",
                  url: url,
                  data: form.serialize(), // serializes the form's elements.
                  success: function (data) {
    
    
    
                    console.log('Submission was successful.');
                    console.log(data);
    
                          if(data.res == 1){
                            $('#groupModal').modal('hide');  
                            location.reload(); 
                         //   show_toast('Group was Created',data.msg,'success');  
                          
                          }
                    },
                        error: function (data) {
                            console.log('An error occurred.');
                            console.log(data);
                        },
                });
      
});
      



//save card ajax  
$("#cardform").submit(function(e) {
      
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');

    $.ajax({
          type: "POST",
          url: url,
          data: form.serialize(), // serializes the form's elements.
          success: function (data) {



            console.log('Submission was successful.');
            console.log(data);

                  if(data.res == 1){
                    $('#cardModal').modal('hide');  
                    location.reload(); 
                   // show_toast('card was Created',data.msg,'success');  
                  
                  }else
                  {
                    show_toast('unable to create card ',data.msg,'error');  
                  }
            },
                error: function (data) {


                    console.log('An error occurred.');
                    console.log(data);
                },
        });

});





 function load_groups(Url,gid){


    $('#group_id')
    .find('option')
    .remove();

    $.ajax({
        type: "GET",
        url: Url,
        data: {}, // serializes the form's elements.
        success: function (data) {
    
            $.each(data, function(i, item) {
            if(item.id  == gid){

                  $('#group_id').append($("<option></option>")
                  .attr("value", item.id)
                  .attr("selected", "selected") 
                  .text(item.name)); 



            }else{
                  $('#group_id').append($("<option></option>")
                  .attr("value", item.id)
                  .text(item.name)); 

            }







            });
          }
      });
    
}


function send_get_ajax(url,result){

      $.ajax({
          type: "GET",
          url: url,
          data: {}, // serializes the form's elements.
          success: function (data) {
            result(data);
            }
        });
      
  }
var gurl ="";


function seturl(url)
{

      gurl = url;
}
function delete_card(){


      send_get_ajax(gurl,function(data){

            if(data.res == 1){
                  $('#delete_cardModal').modal('hide');  
                 // show_toast('card was Deleted',data.msg,'success');  
                  location.reload(); 
                }else
                {
                  show_toast('unable to create card ',data.msg,'error');  
                }
      });
}


function search(url){
      
      
      text_search = $('#text_search').val();
      location.href = url+text_search;
}