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
        text: "You can recover you file from Trash!",
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
                me.removeClass("fa-heart-o")
                me.addClass("fa-heart")
            } else {
                me.removeClass("fa-heart")
                me.addClass("fa-heart-o")
            }
        },
        error: function(error) {
            console.log(error);
        }
    })
})
$(document).on("click", ".open-file", function() {
    var url = $(this).data("url");
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
            me.removeClass("fa-heart")
            me.addClass("fa-heart-o")
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
            me.removeClass("fa-heart")
            me.addClass("fa-heart-o")
            me.parent().parent().remove();
        },
        error: function(error) {
            console.log(error);
        }
    })
})