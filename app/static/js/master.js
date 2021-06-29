$(document).ready(function(){
  $("#manage_existing_users").dataTable({"order":[]});
  $("#all_users").dataTable({"order":[]});
  $("#app_list").dataTable({"order":[]});
  

  $(".delete-user").click(function(e){
    e.preventDefault();
    let user_id = $(this).attr('userid');
    let hrefUrl = $(this).attr('href');
    var permission = confirm("This will delete user " + user_id + ". Do you want to continue?");
    if (permission) {
        window.location = hrefUrl;
    }

  });
  $(".delete-login-user").click(function(e){
    e.preventDefault();
    let user_id = $(this).attr('userid');
    let hrefUrl = $(this).attr('href');
    var permission = confirm("This will delete user " + user_id + ". Do you want to continue?");
    if (permission) {
        window.location = hrefUrl;
    }

  });
  $(".delete-app").click(function(e){
    e.preventDefault();
    let app_id = $(this).attr('id');
    let hrefUrl = $(this).attr('href');
    var permission = confirm("This will delete app " + app_id + ". Do you want to continue?");
    if (permission) {
        window.location = hrefUrl;
    }

  });
  
  $(function() {
    $('input[name="date_range"]').daterangepicker({
      opens: 'right'
    }, 
    function() {
      // start_date=start.today()
      // end_date=end.today()-timedelta(days=7)
      // console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
    });
  });
});