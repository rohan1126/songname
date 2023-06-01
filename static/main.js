    $(document).ready(function() {
          updateCurrentlyPlaying();
          setInterval(updateCurrentlyPlaying, 1000); // Update every 1 second
        });

        function updateCurrentlyPlaying() {
          $.getJSON('/currently-playing', function(data) {
            if (data.track_name === 'No track currently playing') {
              $('#track-info').text(data.track_name);
              $('#album-cover').attr('src', '');
              $('#progress-bar').hide();
              $('#track-times').hide();
              $('body').css('background-image', '');
            } else {
              $('#track-info').text(data.track_name + ' - ' + data.artist_name);
              $('#album-cover').attr('src', data.album_cover_url);
              $('#progress-bar').show();
              $('#track-times').show();
              var progress = (data.progress_ms / data.duration_ms) * 100;
              animateProgressBar(progress);
              setBlurredBackground(data.album_cover_url); // Blur the image
              updateTrackTimes(data.progress_ms, data.duration_ms);
            }
          });
        }


        function setBlurredBackground(imageUrl) {
          $('.background').css('background-image', 'url(' + imageUrl + ')');
        }


        function animateProgressBar(progress) {
          var progressBar = $('#progress-bar .progress');
          progressBar.stop().animate({ width: progress + '%' }, 500);
        }

        function updateTrackTimes(progressMs, durationMs) {
          var progressSec = Math.floor(progressMs / 1000);
          var durationSec = Math.floor(durationMs / 1000);
          var progressMin = Math.floor(progressSec / 60);
          var durationMin = Math.floor(durationSec / 60);
          var progressSecRemainder = progressSec % 60;
          var durationSecRemainder = durationSec % 60;
          var progressTime = progressMin + ':' + (progressSecRemainder < 10 ? '0' : '') + progressSecRemainder;
          var durationTime = durationMin + ':' + (durationSecRemainder < 10 ? '0' : '') + durationSecRemainder;

          $('#track-times').html('<span>' + progressTime + '</span>' + ' / ' + '<span>' + durationTime + '</span>');
        }
