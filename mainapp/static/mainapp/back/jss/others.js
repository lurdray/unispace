var Script = function() {




  $(function() {

    // Tags Input
    $(".tagsinput").tagsInput();

    // Switch
    $("[data-toggle='switch']").wrap('<div class="switch" />').parent().bootstrapSwitch();

  });




}();
