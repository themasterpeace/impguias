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
        title:'¡¡AVISO IMPORTANTE!!',
        theme:'bootstrap',
        type:color,
        content:msg
      });
      
    }

    