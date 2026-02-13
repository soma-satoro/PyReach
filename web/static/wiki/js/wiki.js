/**
 * Wiki - JavaScript
 * Handles interactive features and enhancements
 */

$(document).ready(function() {
    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        const target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top - 100
            }, 600);
        }
    });

    // Auto-dismiss alerts
    setTimeout(function() {
        $('.alert').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 5000);

    // Search form enhancement
    const searchInput = $('.wiki-search-input');
    if (searchInput.length) {
        let searchTimeout;
        searchInput.on('input', function() {
            clearTimeout(searchTimeout);
            const query = $(this).val();
            
            if (query.length >= 3) {
                searchTimeout = setTimeout(function() {
                    // Could implement live search here
                    console.log('Searching for:', query);
                }, 300);
            }
        });
    }

    // Markdown preview (if editor exists)
    $('#preview-btn').on('click', function(e) {
        e.preventDefault();
        const content = $('#id_content').val();
        
        $.ajax({
            url: '/wiki/ajax/preview/',
            method: 'POST',
            data: {
                content: content,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                $('#preview-area').html(response.html).show();
            },
            error: function() {
                alert('Error generating preview');
            }
        });
    });

    // Confirm delete
    $('.btn-danger[href*="delete"]').on('click', function(e) {
        if (!confirm('Are you sure you want to delete this page? This action cannot be undone.')) {
            e.preventDefault();
        }
    });

    // Category expand/collapse
    $('.category-toggle').on('click', function() {
        $(this).parent().next('.subcategories').slideToggle();
        $(this).find('i').toggleClass('fa-chevron-down fa-chevron-up');
    });

    // Back to top button
    const backToTop = $('<button>')
        .addClass('back-to-top')
        .html('<i class="fas fa-arrow-up"></i>')
        .appendTo('body')
        .hide()
        .on('click', function() {
            $('html, body').animate({scrollTop: 0}, 600);
        });

    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            backToTop.fadeIn();
        } else {
            backToTop.fadeOut();
        }
    });

    // Syntax highlighting for code blocks (if present)
    $('pre code').each(function() {
        $(this).parent().addClass('code-block');
    });

    // Table of contents generator
    const $article = $('.wiki-article-content');
    if ($article.length && $article.find('h2, h3').length > 2) {
        const $toc = $('<div>').addClass('table-of-contents');
        const $tocTitle = $('<h3>').text('Table of Contents');
        const $tocList = $('<ul>');

        $article.find('h2, h3').each(function(index) {
            const $heading = $(this);
            const id = 'heading-' + index;
            $heading.attr('id', id);

            const $li = $('<li>');
            const $link = $('<a>')
                .attr('href', '#' + id)
                .text($heading.text());

            if ($heading.is('h3')) {
                $li.addClass('toc-sub');
            }

            $li.append($link);
            $tocList.append($li);
        });

        $toc.append($tocTitle).append($tocList);
        $article.prepend($toc);
    }

    // Copy code blocks
    $('pre').each(function() {
        const $pre = $(this);
        const $button = $('<button>')
            .addClass('copy-code-btn')
            .html('<i class="fas fa-copy"></i> Copy')
            .on('click', function() {
                const text = $pre.find('code').text();
                navigator.clipboard.writeText(text).then(() => {
                    $button.html('<i class="fas fa-check"></i> Copied!');
                    setTimeout(() => {
                        $button.html('<i class="fas fa-copy"></i> Copy');
                    }, 2000);
                });
            });
        $pre.before($button);
    });

    // Tag filter (if on index/category page)
    $('.tag-filter').on('click', function(e) {
        e.preventDefault();
        const tag = $(this).data('tag');
        const $pages = $('.wiki-page-card');
        
        if (tag === 'all') {
            $pages.show();
        } else {
            $pages.hide();
            $pages.filter('[data-tags*="' + tag + '"]').show();
        }

        $('.tag-filter').removeClass('active');
        $(this).addClass('active');
    });

    // Enhanced search with filters
    $('.search-toggle-filters').on('click', function() {
        $('.search-filters').slideToggle();
        $(this).find('i').toggleClass('fa-chevron-down fa-chevron-up');
    });
});

