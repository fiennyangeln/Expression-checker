function check_answer()
{
  var value ={};
  $("#resultgroup").hide();
  var value_1 = document.getElementById("hidden-1").value;
  var value_2 = document.getElementById("hidden-2").value;
  value['value_1'] = value_1;
  value['value_2'] = value_2;
  var csrftoken = $.cookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  console.log(JSON.stringify(value));
  $.ajax('/check_answer/', {
      type : 'POST',
      contentType : 'application/json',
      data : JSON.stringify(value),
      success : function(data) {
          var JSONresult = JSON.parse(JSON.stringify(data));
          var result = JSONresult['result'];
          display_result(result);
      },
      error : function(data, status, error){
          display_error(error);
    }
  }
);
};
function clear_answer()
{
  let MQ = MathQuill.getInterface(MathQuill.getInterface.MAX);
  //MQ.MathField($('.mathquill-editable')).latex("");
  $('.mathquill-editable').latex("");
  $('#hidden-1').val('');
  $('#hidden-2').val('');
};
function display_result(result){
  var paragraph = document.getElementById("result");
  if (result){
      paragraph.innerHTML = "<p>They are both same expression. </p>";
  }
  else {
      paragraph.innerHTML = "<p>It is a two different expression. </p>";
  }
  var paragraphheader = document.getElementById("resultheader");
  if (result){
      paragraphheader.innerHTML = "Yes, they are.";
  }
  else {
      paragraphheader.innerHTML = "No, they arent";
  }
  $("#resultgroup").show();
};

function display_error(error){
  console.log(error);
};
