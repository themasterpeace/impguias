function mensaje(msg,color='green')
    {
      if (color=="success")
      {
        color="green";
      }
      if (color=="error")
      {
        color="red";
      }


      $.alert({
        title:'',
        theme:'supervan',
        type:color,
        content:msg
      });
      
    }

    