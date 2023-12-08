function mensaje(msg,color)
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
        title:'Mensaje!',
        theme:'dark',
        type:color,
        content:msg
      });
      
    }

    