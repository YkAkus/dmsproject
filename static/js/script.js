let embed = document.getElementById('embed1');
var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};


$(document).on("click", ".logout", function() {
    Swal.fire({
        title: 'Are you sure want to logout?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, logout'
    }).then((result) => {
        if (result.isConfirmed) {
            window.open("/accounts/logout/", "_self")
        }
    })
})


$(document).on(" click ", ".remove-file", function() {
    me = $(this);
    id = me.data("id");
    Swal.fire({
        title: 'Are you sure?',
        text: "You can remove your file from Trash!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                "url": "/remove-files/",
                "type": "POST",
                "data": {
                    "csrfmiddlewaretoken": csrfcookie(),
                    "id": id
                },
                success: function(response) {
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                    me.parent().parent().parent().parent().remove();
                },
                error: function(error) {
                    console.log(error);
                },
            });
        }
    })
})
$(document).on(" click ", ".remove-folder", function() {
    me = $(this);
    id = me.data("id");
    Swal.fire({
        title: 'Are you sure?',
        text: "You can remove your folder from Trash!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                "url": "/remove-folders/",
                "type": "POST",
                "data": {
                    "csrfmiddlewaretoken": csrfcookie(),
                    "id": id
                },
                success: function(response) {
                    Swal.fire(
                        'Deleted!',
                        'Your folder has been deleted.',
                        'success'
                    )
                    me.parent().parent().parent().parent().remove();
                },
                error: function(error) {
                    console.log(error);
                },
            });
        }
    })
})

$(document).on("click", ".make-fav", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/make-fav/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            if (response["data"]) {
                me.removeClass("text-warning")
                me.addClass("text-secondary")
            } else {
                me.removeClass("text-secondary")
                me.addClass("text-warning")
            }
        },
        error: function(error) {
            console.log(error);
        }
    })
})
$(document).on("click", ".open-file", function() {
    var url = $(this).data("url");
    // window.open(`${url}`,'_self');
    window.location.replace(`${url}`);
})
$(document).on("click", ".preview-pdf", function() {
    var url = $(this).data("url");
    //console.log(url);
    embed.src = url + "#toolbar=1"; 
    // window.open(`${url}`, '_blank');
})
$(document).on("dblclick", ".db-click", function() {
    var url = $(this).data("url");
    console.log(url);
    //embed.src = url + "#toolbar=0";
    window.open(`${url}`, '_blank');
})
$(document).on("click", ".share-file", function() {
    url = $(this).data("url");
    base_url = window.location.origin;
    Swal.fire({
        title: 'Shareable Link',
        text: `${base_url}/${url}`,
    })
})

$(document).on("click", ".make-favs", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/make-fav/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            me.removeClass("text-warning")
            me.addClass("text-secondary")
            me.parent().parent().remove();
        },
        error: function(error) {
            console.log(error);
        }
    })
})

$(document).on(" click ", ".delete-file", function() {
    me = $(this);
    id = me.data("id");
    Swal.fire({
        title: 'Are you sure?',
        text: "You won 't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                "url": "/del-files/",
                "type": "POST",
                "data": {
                    "csrfmiddlewaretoken": csrfcookie(),
                    "id": id
                },
                success: function(response) {
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                    me.parent().parent().remove();
                },
                error: function(error) {
                    console.log(error);
                },
            });
        }
    })
})
$(document).on("click", ".restore-file", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/restore-file/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            me.removeClass("text-warning")
            me.addClass("text-secondary")
            me.parent().parent().remove();
        },
        error: function(error) {
            console.log(error);
        }
    })
})

$(document).on('click', function(e) {
    if ($(e.target).closest(".my-drop-down").length === 0) {
        $(".my-drop-down").hide();
    }
});

