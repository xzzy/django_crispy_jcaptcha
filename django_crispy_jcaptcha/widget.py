from django.forms import Media, MediaDefiningClass, Widget, CheckboxInput
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from django_crispy_jcaptcha import models
from django.conf import settings

import binascii
import uuid
import os, hashlib
import random

class CaptchaImages(Widget):

     def __init__(self, *args, **kwargs):
         self.attrs = {'test': 'test'}


     def render(self, name, value, *args, **kwargs):
         STATIC_URL = settings.STATIC_URL
         JCAPTCHA_EXPIRY_MINUTES=30
         JCAPTCHA_CLEANUP_MINUTES=1440

         if hasattr(settings,'JCAPTCHA_EXPIRY_MINUTES'):
              JCAPTCHA_EXPIRY_MINUTES=settings.JCAPTCHA_EXPIRY_MINUTES

         if hasattr(settings,'JCAPTCHA_CLEANUP_MINUTES'):
              JCAPTCHA_CLEANUP_MINUTES=settings.JCAPTCHA_CLEANUP_MINUTES

         now = datetime.now()
         expiry = now + timedelta(minutes = JCAPTCHA_EXPIRY_MINUTES)
         in_the_past = now - timedelta(minutes=JCAPTCHA_CLEANUP_MINUTES)
         cleanup_captchas = models.Captcha.objects.filter(expiry__lte=in_the_past).delete()

         id_name = 'id_'+name
         images = self.imagelist()
         random.shuffle(images)

         image_selection = images[0]
         captcha = models.Captcha.objects.create(captcha_key=hashlib.md5(os.urandom(32)).hexdigest(),captcha_image=image_selection['image'], image_key_match=image_selection['random_key'],expiry=expiry)

         image_rotation = []
         image_rotation.append(images[0])
         image_rotation.append(images[1])
         image_rotation.append(images[2])
         image_rotation.append(images[3])
         image_rotation.append(images[4])
         image_rotation.append(images[5])
         image_rotation.append(images[6])
         image_rotation.append(images[7])
         image_rotation.append(images[8])
         image_rotation.append(images[9])
         image_rotation.append(images[10])
         image_rotation.append(images[11])
         image_rotation.append(images[12])
         image_rotation.append(images[13])
         image_rotation.append(images[14])
         image_rotation.append(images[15])
         image_rotation.append(images[16])
         image_rotation.append(images[17])
         image_rotation.append(images[18])
         image_rotation.append(images[19])
         image_rotation.append(images[20])
         image_rotation.append(images[21])
         image_rotation.append(images[22])
         image_rotation.append(images[23])

        
         random.shuffle(image_rotation) 
         for im in image_rotation:
             captcha_image = models.CaptchaImage.objects.create(captcha=captcha,captcha_key=im['random_key'],captcha_image=im['image'])

         image_div = ""
         for im in image_rotation:
             image_div = image_div + "<img width='39px' height='39px' id='id_captcha_image_"+im['random_key']+"' onclick="+'"'+"jcaptcha.select('"+id_name+"','"+captcha.captcha_key+"','"+im['random_key']+"');"+'"'+" src='/jcaptcha/image-match/"+im['random_key']+".png' class='jcaptcha-matches' istyle='border: 1px solid #000000; padding: 3px; margin-right: 2px; cursor: pointer;'>"

         htmldata = ""
         htmldata += "<link rel='stylesheet' href='"+STATIC_URL+"/css/jcaptcha/style.css'>"
         htmldata += "<script type='text/javascript' src='"+STATIC_URL+"/js/jcaptcha/jcaptcha.js'></script>"
         htmldata += "<div id='jwidget_div_"+name+"'>"
         htmldata += "<div>Please select the matching image below: <img width='39px' height='39px' src='/jcaptcha/image-selection/"+captcha.captcha_key+".png' style='border: 1px solid #000000; padding: 3px; margin-right: 2px;'></div>"
         htmldata += "<div><br></div>"
         htmldata += "<div><b>Match selection</b></div>"
         htmldata += "<center><div style='min-width: 250px; max-width: 300px;'>"+image_div+"</div></center>"
         htmldata += "<div><input type='hidden' name='"+name+"' id='"+id_name+"'>"
         htmldata += "<div><br></div>"
         htmldata += "<div><br></div>"

         return format_html(htmldata)


     def imagelist(self):

         if settings.JCAPTCHA_IMAGE_LIST == 'jcaptcha2': 
               images = [{ 'image' : '/static/images/jcaptcha2/paw-prints-feet-footprint-animal-33927.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/blossom-daizy-flower-smell-33866.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/herb-leaf-plant-tree-green-nature-environment-33900.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/rooster-food-chicken-chick-animal-33933.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dog-face-tongue-human-friend-33944.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dark-moon-with-face-phase-33873.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sheep-ewe-goat-horn-animal-33946.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/honeybee-bee-insect-honey-bug-33902.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/fish-pisces-sea-food-aquatics-animal-33888.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/palm-tree-green-nature-plant-33924.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/palm-tree-green-nature-plant-33924.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/last-quarter-moon-half-planet-33908.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/last-quarter-moon-dark-half-33975.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/front-facing-baby-chick-chicken-food-33971.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/waning-gibbous-moon-phase-33967.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/tropical-fish-aquatic-sea-food-33961.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/first-quarter-moon-half-dark-flag-mark-33886.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/glowing-star-glittery-glow-shining-sparkle-33896.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/lady-beetle-insect-ladybird-ladybug-33906.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/first-quarter-moon-with-face-phase-33887.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/fallen-leaf-fall-falling-nature-33942.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cactus-plant-malocactus-cacti-33859.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/decoration-celebration-glass-christmas-33874.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/hamster-face-pet-adopt-cat-33973.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/pig-sus-wild-animal-food-33969.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/pig-face-sus-wild-animal-food-33928.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dizzy-star-shooting-favorite-33876.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/last-quarter-moon-with-face-phase-33909.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/bright-button-sun-dim-rays-33865.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/elephant-wild-animal-mammal-huge-33882.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/elephant-wild-animal-mammal-huge-33882.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/tiger-wild-animal-forest-king-33962.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/blowfish-fish-sea-food-aquatic-animal-33864.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/full-moon-phase-dark-33890.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/bug-caterpiller-insect-harm-33938.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dragon-fairy-tale-war-33877.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/tiger-face-wild-animal-forest-king-33959.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/pig-nose-sus-ani-al-food-33929.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/droplet-drop-water-save-33879.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         #{ 'image' : '/static/images/jcaptcha2/globe-showing-americas-eart-33894.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dragon-face-fairy-tale-war-wild-animal-33878.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/ant-insect-bug-formicidae-small-33858.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/eight-pointed-star-favorite-33883.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cow-animal-mammal-milk-33914.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/horse-face-hairy-animal-33904.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/boar-pig-sus-animal-wild-33867.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/celebration-halloween-jack-lantern-christmas-33891.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dolphin-flipper-mammal-show-aquatic-33943.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/snake-bearer-ophiuchus-serpent-zodiac-33947.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/panda-face-wild-animal-33925.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/snowman-without-snow-cold-christmas-33948.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/wolf-face-wild-animal-33978.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cat-face-pet-adopt-animal-human-friend-33939.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sparkles-star-decoration-celebration-christmas-crackers-33952.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cow-face-animal-mammal-milk-33940.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sun-behind-large-cloud-brightness-weather-rainy-33958.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/ear-of-corn-maize-maze-food-33885.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/whale-aquatic-mammal-animal-33974.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/goat-capricorn-mammal-wild-animal-33898.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sheafofrice-ear-grain-rice-33945.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/full-moon-with-face-phase-33893.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/rose-flower-bloosom-smell-plant-33935.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/poodle-dog-cute-pet-adopt-33930.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/moon-viewing-ceremony-celebration-33917.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/koala-bear-lazy-honey-wild-animal-33903.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/camel-dromedary-hump-mammal-animal-33871.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/leaf-fluttering-wind-blow-flutter-33907.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/mouse-rat-test-animal-science-33920.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/chicken-baby-food-chick-33911.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/fire-flame-tool-light-spark-33937.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/horse-jockey-racing-animal-wild-33905.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/seedling-young-leaf-green-environment-nature-33936.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/tulip-flower-rose-plant-smell-33964.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cloud-weather-rainy-season-33868.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/deciduous-tree-shedding-shape-green-nature-33875.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/spouting-whale-aquatic-water-mammal-animal-33953.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dog-pet-adopt-human-friend-animal-33941.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/turtle-terrapin-tortoise-terrestrial-land-shield-33963.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/rabbit-face-mammal-test-33932.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/baby-chick-chicken-food-animal-meat-33863.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/snail-water-aquatic-land-terrestrial-33949.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/umbrella-with-rain-drops-rainy-season-33966.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/waxing-gibbous-moon-dark-33977.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/leopard-animal-big-cat-wild-33910.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/mouse-face-rt-animal-test-science-33919.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/rabbit-animal-test-mammal-33931.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/mouse-rat-test-animal-33918.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         #{ 'image' : '/static/images/jcaptcha2/globe-showing-europe-africa-earth-33897.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/penguin-aquatic-animal-mammal-33926.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sun-bright-rays-sunny-weather-33960.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/octopus-aquztic-animal-mammal-octopoda-33923.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/ox-bull-taurus-intact-wild-animal-33922.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/two-hump-camel-bactrian-animal-mammal-33965.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/brightness-dim-low-button-bright-33869.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/frog-face-animal-aquatic-33968.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/globe-showing-asia-australia-earth-33895.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cat-pet-wild-animal-33912.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sunflower-flower-plant-bloosom-smell-33956.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/hibiscus-plant-bloosom-smell-33901.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sparkle-decore-dcoration-crackers-33951.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/waxing-crescent-moon-phase-dark-33976.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/monkey-primate-tail-human-forest-33916.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/monkey-face-human-primate-33915.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/dog-pet-adopt-human-friend-animal-33941 (1).png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/four-leaf-clover-green-tree-33889.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/crocodile-aquatica-animal-wild-33872.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/bird-feather-aves-animal-33860.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/spiral-shell-aquatic-water-art-33954.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/new-moon-phase-dark-mark-33921.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/earth-globe-meridians-world-33880.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/chestnut-plant-nut-food-healthy-33892.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/crescent-moon-mark-phase-33870.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/eight-spoked-asterisk-purple-information-33881.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sun-with-face-smiley-ray-33955.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/snowflake-cold-snow-flake-winter-33950.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/hatching-chick-baby-egg-new-born-33899.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/bear-face-animal-wild-33861.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/cherry-blossom-flower-smell-33913.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/maple-leaf-falling-nature-33970.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha2/sweat-droplets-drop-rain-33957.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                        ]
         else:
               images = [{ 'image' : '/static/images/jcaptcha/headphones-human.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/lighter.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/bomb-grenade.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/dating-rose.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/golf-hole.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/skull-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/coffee-cold.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/rat.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/rooster.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/cog.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/pin.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/office-work-wireless.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/outdoors-tree-valley.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/plane-trip-international.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/programming-flag.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/whale-body.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/send-email-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/shop-cashier-man.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/shop-cashier-woman.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/show-hat-magician-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/stamps-famous.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/tablet-touch.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/target-center-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/warehouse-storage-3.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/insurance-card.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/landmark-japan-shrine.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/laptop-smiley-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/email-action-receive.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/footwear-heels-ankle.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/hammer-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/gauge-dashboard-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/love-boat.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/maps-pin.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/medical-personnel-doctor.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/megaphone-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/monkey.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/mood-happy.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/mouse.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/mobile-phone-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                         { 'image' : '/static/images/jcaptcha/nautic-sports-sailing-person.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},

                        ]
         return images          


def CaptchaValidation(captcha_value, forms):
    now = datetime.now()
    captcha_valid = False
    captcha_split = captcha_value.split(':')
    if len(captcha_split) == 2:
        if models.Captcha.objects.filter(captcha_key=captcha_split[0], image_key_match=captcha_split[1],expiry__gte=now).count() > 0:
            print ("captcha valid")
            captcha_valid = True 
            cap = models.Captcha.objects.filter(captcha_key=captcha_split[0], image_key_match=captcha_split[1],expiry__gte=now)
            for c in cap:
                c.expiry=now
                c.save()
            pass
        else:
            cap = models.Captcha.objects.filter(captcha_key=captcha_split[0],expiry__gte=now)
            for c in cap:
                c.expiry=now
                c.save()

            raise forms.ValidationError('Captcha selection incorrect,  please try again.')
    else:
        raise forms.ValidationError('Please select matching captcha picture.')
    
    return captcha_valid






