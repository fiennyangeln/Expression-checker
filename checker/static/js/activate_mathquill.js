
function activateMathquill() {
    var dirty_span_list = document.getElementsByTagName("span");
    var span_list = [];
    //Get the ID of all answer box span
    for (var i = 0; i < dirty_span_list.length; i++) {
        var span_id = dirty_span_list[i].id;
        var position = span_id.indexOf("value");
        if (position != -1) {
          span_list.push(span_id);
        }
    }
    no_span = span_list.length;
    for (var i = 0; i < no_span; i++) {
        span_details = span_list[i].split("-");
        //Remove the keyword 'answer' from the list
        span_details = span_details.slice(1);
        activateMathquillSpan(span_details);
    }
};

function activateMathquillSpan(i) {
    source_id = 'value-' + i;
    target_id = 'hidden-' + i;
    var mathFieldSpan = document.getElementById(source_id);
    var latexSpan = document.getElementById(target_id);
    var MQ = MathQuill.getInterface(2); // for backcompat
    var mathField = MQ.MathField(mathFieldSpan, {
        spaceBehavesLikeTab: true, // configurable
        supSubsRequireOperand: true,
        charsThatBreakOutOfSupSub: '+-=<>',
        autoCommands: 'pi theta sqrt sum',
        handlers: {
            edit: function() { // useful event handler
                latexSpan.value = mathField.latex(); // simple API
            }
        }
    });
};

$(document).ready(function() {
    activateMathquill();
});
