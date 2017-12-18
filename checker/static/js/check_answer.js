function check_answer()
{
  var value ={};

  var value_1 = document.getElementById("value-1").textContent;
  var value_2 = document.getElementById("value-2").textContent;
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

function display_result(result){
  var paragraph = document.getElementById("result");
  if (result){
      paragraph.innerHTML = "<p>True</p>";
  }
  else {
      paragraph.innerHTML = "<p>It is a two different element</p>";
  }
};

function display_error(){
  console.log(error);
};
