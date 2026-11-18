with open('thankyou.html', 'r', encoding='utf-8') as f:
    t_html = f.read()

t_html = t_html.replace('../../../getOriginUrl.js', 'getOriginUrl.js')
t_html = t_html.replace('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.css', 'landing_page/assets/vendors/slick/slick.css')
t_html = t_html.replace('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js', 'landing_page/assets/vendors/slick/slick.min.js')

with open('thankyou.html', 'w', encoding='utf-8') as f:
    f.write(t_html)

print("Updated thankyou.html!")
