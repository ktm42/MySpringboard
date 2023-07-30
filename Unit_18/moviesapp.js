$(document).ready(function(){
    $('#submitTitle').on('submit', function(e) {
        e.preventDefault();
        const movie = $('#movieTitle').val();
        let newMovie = $('<li class="movieList"></li>');        
        let button = $('<button>Delete</button>');    
          
        newMovie.html(movie).append(function() {
            let rating =$('.slider')
            console.log('rating');
            $('#movies').append(newMovie);
        });
        
         //putting in ul
        
         $(this).trigger('reset');
       
        $('button').on('click', function(){        
            $(newMovie).remove(); 
        });


         
    });

});
