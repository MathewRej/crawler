function build_lyrics(lyrics) {
    ret = $(`<p>
    <h4> Lyrics for ${lyrics.name} </h4>
</p>
<p>
    <em><center>${lyrics.lyrics.replaceAll("\n", "<br/>")}<center/><em/>
</p>`)

    return ret;
}

function main(){
    console.log("Hello!!!!!")
    
    $("a.songlink").click(function (ev){
        console.log(ev)
        ev.target.href.replace(ev.target.innerText)
        // url = ev.target.href.replace("/song/","/lyrics/")
        $("div.lyrics").text("Loading......")
        $.ajax({
            url: ev.target.href,
            dataType: 'json',
            success: function(data, textStatus, jqXHR){
            $("div.lyrics").html(build_lyrics(data.song));
            var text = ev.target.innerText;
                    var parent = ev.target.parentNode;
                    ev.target.remove(); 
                    $(parent).html(text)
                    $(".songname").html(`<a
                    class = "songlink" href="/song/${$(".songname").attr("id")}">${$(".songname").text()}<a/>`)
                    
                    // var link = ev.target.href
                    

                //    $("li.songname").wrap('<a href="' + ev.target.href + '"></a>')
                
            }
            
        }) 
        
        ev.preventDefault();
    });

}
$(main);


