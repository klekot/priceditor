def html_show(html_text):
    f_header = open("header.html", 'r')
    f_html = open("page.html", 'w')
    f_html.write(f_header.read())
    f_html.close()

    f_html = open("page.html", 'a')
    f_html.write(html_text.encode('cp1251', errors='replace'))
    f_html.close()

    f_footer = open("footer.html", 'r')
    f_html = open("page.html", 'a')
    f_html.write(f_footer.read())
    f_html.close()