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
        title:'¡¡Lo sentimos!!',
        theme:'bootstrap',
        type:color,
        content:msg
      });
      
    }

    