# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_engine"))
from sitegen import *

EMAIL = "ficonvention@gmail.com"
SITE = dict(
    name="Floating Island", domain="www.floatingisland.co.kr",
    brand_main="FLOATING ISLAND", brand_sub="세빛섬 플로팅아일랜드 컨벤션",
    desc="Floating Island Convention — Seoul's representative MICE unique venue on the Han River at Some Sevit (Sebitseom). Convention Hall, Villa de Noche, Vista, Terrace Room, Rive Gauche, Medici, Orchid, Garden, Rooftop.",
    og="2649b2_cdd8e2a0c9904b90963531e652bdfa98~mv2.jpeg",
    address="Some Sevit, 650 Banpo-dong, Seocho-gu, Seoul, Korea (서울 서초구 올림픽대로 2085-14 세빛섬)",
    tel="+82 2 537 2440", tel_raw="+8225372440", fax="+82 2 537 2499", email=EMAIL,
    legal="Floating Island Convention",
    social=[("Instagram", "https://www.instagram.com/marinaparkwedding", IG_SVG), ("Facebook", "https://www.facebook.com/Floatingisland1", FB_SVG)],
    favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0f1b2d"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#c9b27a">F</text></svg>',
    nav=[
        ("index.html", "Home", [("index.html#about", "About"), ("index.html#gallery", "Gallery"), ("index.html#things", "Things to do")]),
        ("convention-hall.html", "2F Convention Hall", [("villa-de-noche.html", "2F Villa de Noche")]),
        ("vista.html", "3F Vista", [("terrace-room.html", "3F Terrace Room"), ("rive-gauche.html", "3F Rive Gauche"), ("medici.html", "3F Medici"), ("orchid.html", "3F Orchid")]),
        ("garden.html", "4F Garden", []),
        ("rooftop.html", "Rooftop", []),
        ("contact.html", "Contact", []),
    ],
)

THEME = """:root{
  --ink:#0f1b2d; --ink-soft:#4b5666; --line:#e2e4e8; --paper:#ffffff; --cream:#f3f5f8;
  --gold:#c9b27a; --gold-deep:#9d8650; --sky:#daeef3;
  --serif:"Cormorant Garamond",Georgia,serif; --sans:"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  --wrap:1180px; --header-h:76px;
}
.site-footer{background:#0b1522}.cta-band{background:#0f1b2d}
"""

J = lambda ids, o="L": [(f"2649b2_{i}~mv2.jpg", o) for i in ids]
GALLERY = J(["99a3fbbb08834b889e963577c4098b8b","016a6ee085a148b4bb940f233b61aa6b","11da3a35b9b245029d8ca81934c535e5","40048dd70090440aba26bbe3f09862bd","b686fceb479747b98d297dfe82230403","824eef1897e74d4a93619d976b45c749","efbc038131b04f788986e1c379e19b87","2d7ddf7cdae74fd5b6b3e366aeb7ccc8","8b0e3342fe104891bc968818eb62e28a","a8bf0c65951a4af4b117a6cba328f313","93b94d9bb3484c2ea680839dbc5ddec0","ac74961293094d51997a61d2a0fc424f","72c037be87c74f0ea96e85ca04689aed","9123466032214c8b8d3dcc37f7971d71","7d1eb345998641d593c91e27a0450f9a","793d210cc8bc41d2b114e563d5854d6b","e3ad29b5e3e649e88021b6be1026b55b","c39a7b89f1584a4398fc4dd7c9234994","008d9ee815b54c76a1cda89a26a55cc5","8e49121b816646ea865e8c1940c14c78","e3565923e9c4404c9cdfe89ddbd0be8b","fa1b3d2a4c0d4f2093d4c45d90668bb2","873e6fc6bc5549ea8569959ab4b60b55","561bd9ee604f41c4a8755a61dfbe0f3a"])

HALLS = [
    # file, floor, name, kr, capacity, blurb, hero, imgs(list of (id, orient))
    ("convention-hall.html", "2F", "Convention Hall", "컨벤션홀", "Up to 600 pax", "The Convention Hall is the largest banquet hall at Floating Island for large-scale international conferences, gala dinners, award ceremonies and weddings, accommodating up to 600 guests with a full stage, LED screen and sound system — and floor-to-ceiling views of the Han River.", "2649b2_0a45731667d6441a83649c17c52f34a1~mv2.jpg",
     J(["77f9713e03dc409cadf3235963ec3626","7650167a98a34411a69c805312762a95","7771d805b83b4bb49a9b45387ff649a3","b050a05e894c4aac800b66a336a4de35","eba4b166667d4183b1f64d961bbef14a","bf8e3684c7b74ac7afa3b14569ad2392","b117f1153f404579ad615390cdb47024"])),
    ("villa-de-noche.html", "2F", "Villa de Noche", "빌라 드 노체", "Private banquets", "At Villa de Noche we strive to create unforgettable experiences, weaving together elegance, versatility and personalized service to ensure your event is truly exceptional — an intimate banquet room for dinners, receptions and private celebrations.", "2649b2_cdf8b09730574989a5d585e31ea2d6ea~mv2.jpg",
     J(["acadc7d579b8405fbc8e200a6379d7f6","b9375e5986f3453c8369d3f2e90986a5","33fcbc16879f413ba8d0b0cbc0373154","95900cd9b5d94b6c9f687a75faf053d5","fef0c91bed334433bae446570d3f1f78","6d13ab22d4364b39abb4f45a31ba159e","3009350750654bf689717ce5703deaec","a3ed288127ae449696fad955445050b6"])),
    ("vista.html", "3F", "Vista", "비스타", "Weddings · Conferences", "A venue with a vista creates a remarkable ambiance. Overlooking the Han River and the Banpo Bridge Rainbow Fountain, Vista provides a memorable backdrop for weddings, conferences and special occasions, leaving guests with lasting impressions.", "2649b2_0c38784a7be548199fa50e6c66e9b4ea~mv2.jpg",
     J(["93b94d9bb3484c2ea680839dbc5ddec0","a8bf0c65951a4af4b117a6cba328f313","a07c073494d54d0488f5e5974f2c1db7","49799497b310482a94a2fedfc57a5420","b797b69ae32648b7840cecce29270add","9409dec9c57841e098c6cd225abf2710","af20468dc8be42ad9a419ffd6105b1b7","6ee84862030e4a5db823d8abfa493482","31bf26bcaf5043c7978669b1c4786966","24796eace24d458d84c562d1168a57d7"])),
    ("terrace-room.html", "3F", "Terrace Room", "테라스룸", "30 – 60 guests", "This elegant space is perfect for private dining, meetings and intimate family gatherings, accommodating 30 to 60 guests. With its inviting ambiance and versatile layout, the Terrace Room provides a charming and exclusive setting for your special occasions.", "2649b2_fb363146a29b434abb94012b61855123~mv2.jpg",
     J(["035a54e867a9492caec8d3f103a7ec13","e0408f8cb4314b68960aa19aa77ef6a9","b4dffb3454854f0886628e4487e685be"])),
    ("rive-gauche.html", "3F", "Rive Gauche", "리브 고쉬", "Receptions · Dinners", "From its elegant architecture to its carefully curated interiors, every detail has been designed to evoke the timeless allure of the iconic Parisian district. Rive Gauche combines that essence with modern amenities, creating an extraordinary setting for memorable events, celebrations and gatherings.", "2649b2_c38a145f9e354b64a62be4b98620e917~mv2.jpg",
     J(["e63e82216e0e42debd79aacfde92e6d4","25302c19d7c94917a999c3b41c847bd4","1bab4e9ee6bf4b0595ff9f6401b324d0"])),
    ("medici.html", "3F", "Medici Room", "메디치룸", "VIP · Private", "The Medici Room encapsulates the essence of Italian grandeur, transporting guests to a realm where luxury and style converge effortlessly. Immerse yourself in an ambiance of unparalleled refinement — an exclusive sanctuary for discerning guests seeking a truly transcendent experience.", "2649b2_95ad344545704b3ca6ec3730aecce3fe~mv2.jpg",
     [("2649b2_873e6fc6bc5549ea8569959ab4b60b55~mv2.jpg","L"),("2649b2_24c87f5b551e438db2e213350f2ae178~mv2.jpg","P")]),
    ("orchid.html", "3F", "Orchid Room", "오키드룸", "Meetings · Small banquets", "A refined room named after the orchid — calm, bright and private. Ideal for board meetings, VIP luncheons and small family banquets, with the same river-side setting as the rest of the third floor.", "2649b2_e2da3949158945758890a51d67483c92f000.jpg",
     [("2649b2_e2da3949158945758890a51d67483c92f000.jpg","P")]),
    ("garden.html", "4F", "Garden", "4층 가든", "Outdoor · Cocktail", "An open-air garden on the fourth floor with the Han River on every side. Perfect for cocktail receptions, pre-dinner gatherings, outdoor ceremonies and sunset photo moments before the Rainbow Fountain show.", "2649b2_7d1eb345998641d593c91e27a0450f9a~mv2.jpg",
     J(["2202cb7fc47149c8a5290498f1d86faa","9123466032214c8b8d3dcc37f7971d71","f034d6edd77349eaac2443dddf9abc9d"], "P")),
    ("rooftop.html", "5F", "Rooftop", "루프탑", "Night view · Parties", "The highlight of this breathtaking rooftop is the magnificent Rainbow Fountain, gracefully dancing in harmony with the evening breeze. With its seamless blend of natural beauty and modern marvels, our rooftop is the perfect vantage point for Seoul's sparkling nightscape.", "2649b2_72c037be87c74f0ea96e85ca04689aed~mv2.jpg",
     J(["7ccdbc8d93964b3d8beae3a75f8d1ecb","c9bfc349579448e0abe839ea834f9ef0","874d596b91c6405a80f70bcf4f30a881"], "P")),
]

def hall_card(h):
    f, floor, name, kr, cap, blurb, hero, imgs = h
    return f'<a class="hall" href="{f}"><img src="{wix(hero, 900, 640)}" loading="lazy" alt="{name}"><div class="hall-txt"><span class="eyebrow">{floor} · {cap}</span><h3>{name}</h3><p>{kr}</p></div></a>'

home = f"""
<section class="hero" style="background-image:url('{wix('2649b2_cdd8e2a0c9904b90963531e652bdfa98~mv2.jpeg', 1920, 1280)}')">
  <div class="hero-inner">
    <p class="eyebrow">Seoul · Han River · Some Sevit</p>
    <h1>Floating Island<br>Unique Venue</h1>
    <p class="lead">Seoul's representative MICE unique venue on the Han River</p>
    <div class="hero-cta">
      <a class="btn btn-light" href="#halls">Explore the venue</a>
      <a class="btn btn-outline" href="contact.html">Inquiry</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap split">
    <div class="split-img"><img src="{wix('2649b2_28eff81768df47c9ac05f98ecae63c57f000.jpg', 1100, 733)}" loading="lazy" alt="Floating Island"></div>
    <div class="split-text">
      <p class="eyebrow">About</p>
      <h2>Seoul, the world's representative MICE Unique Venue</h2>
      <p>Located at the end of Banpo Bridge beside the Rainbow Fountain, Some Sevit Floating Island was built as part of the Han River Renaissance Project to establish a world-class landmark for cultural events on the Han River. The unique artificial-island platform and the LED lighting on the outer walls create a stunning view of the river.</p>
      <p>Gabit Island — the first island, where Floating Island Convention is located — is a design building that expresses a flower in full bloom: a venue where international conferences, exhibitions, performances and ceremonies are held for guests from home and abroad.</p>
      <a class="btn" href="mailto:{EMAIL}">Inquiry</a>
    </div>
  </div>
</section>

<section class="section alt" id="halls">
  <div class="wrap">
    <p class="eyebrow center">Venue</p>
    <h2 class="center">Halls by floor</h2>
    <div class="hall-grid">{''.join(hall_card(h) for h in HALLS)}</div>
  </div>
</section>

<section class="section" id="gallery">
  <div class="wrap">
    <p class="eyebrow center">Gallery</p>
    <h2 class="center">Events at Floating Island</h2>
    {gallery(GALLERY)}
  </div>
</section>

<section class="section alt" id="things">
  <div class="wrap">
    <p class="eyebrow center">See &amp; Do</p>
    <h2 class="center">Things to do</h2>
    <div class="things">
      <div><img src="{wix('2649b2_8b0e3342fe104891bc968818eb62e28a~mv2.jpg', 800, 540)}" loading="lazy" alt=""><h3>Yacht Tour</h3><p>Ride a yacht and enjoy the night view of the Han River with the cool river breeze. Yachts are available at various times — from bright daylight to sunset to colorful night views.</p></div>
      <div><img src="{wix('2649b2_72c037be87c74f0ea96e85ca04689aed~mv2.jpg', 800, 540)}" loading="lazy" alt=""><h3>Rainbow Fountain</h3><p>Across the full 1,140 m span of Banpo Bridge, water is sprayed to music so that fountain and soundtrack blend in harmony. At night, landscape lighting turns it into a fantastic river nightscape.</p></div>
      <div><img src="{wix('2649b2_7d1eb345998641d593c91e27a0450f9a~mv2.jpg', 800, 540)}" loading="lazy" alt=""><h3>Beer Garden</h3><p>Enjoy the night view of Sebit Island with hand-crafted beer, wine and a variety of food at the Sebit Island outdoor garden with an open view of the Han River.</p></div>
    </div>
  </div>
</section>

{cta("Contact us", "International conferences · Gala dinners · Weddings · Launching events", "Inquiry", "contact.html", ("+82 2 537 2440", "tel:+8225372440"))}
"""

def hall_page(h):
    f, floor, name, kr, cap, blurb, hero, imgs = h
    others = ''.join(f'<a href="{o[0]}">{o[1]} {o[2]}</a>' for o in HALLS if o[0] != f)
    return f"""{page_hero(hero, f'{floor} · {cap}', name, kr, tall=True)}
<section class="section"><div class="wrap narrow prose"><p>{blurb}</p><p class="center cta-inline"><a class="btn" href="contact.html">Inquiry</a> <a class="btn btn-outline-dark" href="tel:+8225372440">+82 2 537 2440</a></p></div></section>
<section class="section alt"><div class="wrap">{gallery(imgs, "gallery cols-3")}</div></section>
<section class="section"><div class="wrap"><p class="eyebrow center">Other halls</p><nav class="jump">{others}</nav></div></section>
{cta("Plan your event at Floating Island", "", "Contact", "contact.html")}"""

contact = f"""
{page_hero('2649b2_793d210cc8bc41d2b114e563d5854d6b~mv2.jpg', 'Floating Island', 'Contact us')}
<section class="section"><div class="wrap split contact-split">
  <div class="split-text">
    <h2>Let's plan your event</h2>
    <p>Tell us the date, number of guests and type of event — we will come back with a tailored proposal.</p>
    <div class="contact-card">
      <h3>FLOATING ISLAND CONVENTION</h3>
      <p>Some Sevit, 650 Banpo-dong, Seocho-gu, Seoul, South Korea<br>서울 서초구 올림픽대로 2085-14 세빛섬</p>
      <p>Tel: <a href="tel:+8225372440">+82 2 537 2440</a><br>Fax: +82 2 537 2499</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
  {contact_form(EMAIL, ["International Conference / MICE", "Gala Dinner / Corporate Banquet", "Wedding", "Launching / Promotion", "Private Party", "Other"])}
</div></section>
<section class="map-section"><iframe title="Floating Island 위치" src="https://www.google.com/maps?q=%EC%84%B8%EB%B9%9B%EC%84%AC&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></section>
"""

PAGES = {"index.html": ("Home", home, True), "contact.html": ("Contact", contact, False)}
for h in HALLS:
    PAGES[h[0]] = (f"{h[1]} {h[2]}", hall_page(h), False)

EXTRA_CSS = """
.hall-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2.5rem}
.hall{display:block;position:relative;overflow:hidden;background:#000}
.hall img{aspect-ratio:3/2;object-fit:cover;transition:.6s;opacity:.92}
.hall:hover img{transform:scale(1.04);opacity:1}
.hall-txt{position:absolute;left:0;right:0;bottom:0;padding:1.2rem 1.4rem;color:#fff;background:linear-gradient(to top,rgba(10,16,26,.85),transparent)}
.hall-txt .eyebrow{color:var(--gold);margin-bottom:.2em}.hall-txt h3{margin:0;font-size:1.6rem}.hall-txt p{margin:0;font-size:.85rem;opacity:.85}
.things{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2.5rem}
.things img{aspect-ratio:3/2;object-fit:cover;margin-bottom:1rem}.things p{color:var(--ink-soft);font-size:.93rem}
.jump{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;justify-content:center;padding:.5rem 0 0;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase}
.jump a{border-bottom:1px solid transparent;padding:.2rem 0}.jump a:hover{border-color:var(--gold)}
@media (max-width:820px){.hall-grid,.things{grid-template-columns:1fr}}
"""

if __name__ == "__main__":
    build(SITE, PAGES, os.path.dirname(os.path.abspath(__file__)), THEME + EXTRA_CSS)
