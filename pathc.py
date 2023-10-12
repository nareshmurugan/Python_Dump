import os
import time as t
a='''C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Desktop-Control-Using-Hand-Gesture-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/DLLs
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Doc
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Drowsiness detection
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/etc
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Face-Mask-Detection-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Gesture-Control-Media-Player-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hospitalmanagement-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/img2latex-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/include
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kivy
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kmap
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Kmap-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Lib
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/libs
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/protoc-3.18.1-win64
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/PyBirthdayWish-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rebound-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Scripts
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/share
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Sign-Language-Interpreter-using-Deep-Learning-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/SPACE INVADERS
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/success
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tcl
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Tools
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Volume-Control-using-gesture-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/WhatAPhish-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/.py.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/_SPACE_IVADERS_.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/0.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/01.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/1cahce.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/1chace.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/6.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/7.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/8.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/9.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/11.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/30i.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/9489228333.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/a.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/a1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/a2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/aaf.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/academy.db
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ahalam ppt.pptx
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/AIVirtualMouse.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/alan.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/alarm.wav
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Alarm-Clock Sound___(MP3_160K)_1.mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/alert.mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ALITA.ico
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/alita-battle-angel.deskthemepack
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/alternate character.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/amsarani.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ana.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ana2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/anagram.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ar.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/area of circle and rectangle.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/arg.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ask me a question about me.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/atm.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/audio recoder.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/b.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/b.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bb.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/beautiful triplets.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/beautifulsoup.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bgp.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/biggest number of three.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bill division.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/binary seacrh.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/binarySearch.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bitwiseAnd.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/black and white.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/blink_detection_demo.mp4
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Book3.xlsx
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bro.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bubbleSort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bubbleSort1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/BubbleSortnet.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/builtin.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Bullet.wav
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bw_kakashi.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/c.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/c1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/c2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Calculator for python 2.7.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Calculator for python above 2.7.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/camelCase.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cap.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/capitalize.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/captain's room.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/carParking.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cc.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/change.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/chr.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/chrome.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/chromedriver.exe
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/class mll.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/class.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/class2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/climib.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/climibing.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cls.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/comple dir.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/concrt140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/countting valleys.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cramers  rule for three solutions.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cramers rule for two variables.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csaa.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csl.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csl2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csv1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csv2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csvb.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csvd.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csve.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/csvf.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cubic.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/cv.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/d.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/d1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dd_new.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dd1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dear comarade.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/debug.log
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dena dance.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/design pdf viewer.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/designer door mat.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/detect t.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/detect_blinks.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/devayosha gift.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/devayosha.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dia.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diagonal differance.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dictionary.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff f.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff f1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff ud.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff uv.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff.3o.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff5.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff6.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/diff7.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/DIFFERENTIATE BY THE INPUT EQUATION.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/DIFFERENTIATE PROGRAM FOR A EQUATION.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/DIFFERENTIATION PROGRAME FOR A QUADRATIC POLYNAMIAL.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/differetiate.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dino.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Dino_runGame.zip
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/disc.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/divisile pairs.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dl.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dl2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/dolphins.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/drawingshapes.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/drawingshapes.py.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/drawingwindow.kv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/drawingwindow.kv.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ein1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/elec.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/email_id checker.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/email_id_checker.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/emma.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/emoji blaster.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/emoji_blaster.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/emoji_python.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/emojiFuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/encode the string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/encryption.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/encryption1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/England.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/exp.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/F TO C.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/f.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/f2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fact.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/factorial.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/factorial2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/feel.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ff.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fff.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fibbonacci squence.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fibo.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/FIBONACCI SERIES.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/FIBONACCI SQUENCE.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fill char.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fizzbuzz.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/flames.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/font_art.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/formate the string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuc.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuch.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuck the format.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuck_the_gmail.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuck2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuckasdgfgaerg.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fuckit.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fucksdf.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fucl.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fun.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/funny string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/funs.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/g.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/g1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Game of Thrones - Main Title -.mp4
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/game of thrones.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gapminder-FiveYearData.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gcd.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gemstone.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/get-pip.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gk.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gm.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/god.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gopal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/grading_round.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/greedy florist.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/grid fuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Grid_challenge.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gSP.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gSP1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/gSP2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/h.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/h1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/h2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/haarcascade_frontalface_default.xml
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hack.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hackerank.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HandTrackingModule.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HAPPY BIRTHDAY HARDIKA.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HAPPY BIRTHDAY HARIKRISHNAN AKKA.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HAPPY BIRTHDAY JASHVANTHY AKKA.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/happy birthday jothika.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HAPPY BIRTHDAY PRIYADHARSHINI.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HAPPY BIRTHDAY SANGAMITHRAI AKKA.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/happy pongal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/happybirthdayjothika.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hardika.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hari.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hash.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/heart.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/heart1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/helloword.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hgggh.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi 3d 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi 3d 3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi 3d.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi april 4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi april.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi april2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi april3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/HI JOTHIKA AKKA.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hi jothikka.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hmd.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu5.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hu6.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/huff.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hufffinal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hufffuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/huffhalf.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/huffman check.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Huffman coding.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/huffman.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/huffnewyear.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/hurdle race.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/i.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/iat cse.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/if elif.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/if syntax.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/image.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/img1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/IMG-20210519-WA0000.png
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/info.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/input.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/insertionSort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/insta post download.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/inverted star.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ip address.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/iruthirsuttru.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jg.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jo 1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jo 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jo.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/joc.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/joe.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jothi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jothikka.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/jumpingOfClouds.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/K. Jothilakshmi.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/k1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/k2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kamali_akka.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kaprekar.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Kivy-1.11.1-cp38-cp38-win_amd64.whl
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kivy1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kmap goal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/kmap.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/l.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/l1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/l3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/l4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/l11.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Labels.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/lawanya.jpg
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/levitate.m4a
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/levitate.wav
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/library.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/LICENSE.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/line print.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/linearSearch.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/list.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/listcom.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/lists.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/listtest.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/loan sanction.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/loan.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/logical operator.c
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/logical operator.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/logo of hackerrank.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/loop.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/luck balance.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/LUST.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/m.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/macsCupsCakes.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mail.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/main.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/making ana.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mani.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/manim1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/manim2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mao.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mapper-2.0.map
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/matrix inversion method.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/matrix row echolan from.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/matrix script.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/matrix_script.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/max array sum.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/max min.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/maximize it.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Mcqs.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mech loan.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/merge_sort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mergeSort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/migrates of birds.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mII1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mII1x.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/milk.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mim fuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/min abs.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/min abs1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/min absolute.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/min of list.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ml1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/mp 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msuic_player shuffle.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msvcp140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msvcp140_1.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msvcp140_2.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msvcp140_atomic_wait.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/msvcp140_codecvt_ids.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/multiset.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/music player.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/music.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/music_player.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/music_player_tab.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/my first game.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/n
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/n.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/na.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/name marker.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/name.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/nested list.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/netrikan.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/new heart.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/NEWS.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Northern Ireland.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/note pad.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/num.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/num2words.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/numpy fuck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/o.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/obdec.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ocv1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/od.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/odd or even.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/oddict.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/oi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ONLINE CLASS SEP 13.xlsx
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/online_sms.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/openner.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ord.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/organization.db
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/os env.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/os1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/os2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/otp.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p@.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p5.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/p8.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pa4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pali.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/palindrome index.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/palindrome.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/panda1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pangram.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/par.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/paru.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/paru2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/paru3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/password.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/path.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pattern.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pdf to audio.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pg1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pg2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pick_element.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pip
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/please help me.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/plus.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pmcq.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pongal.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/prabagar.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/prime checker.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/prime number.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/prod.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/promethues 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/promuthues.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/PSP.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pspp lab.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/py1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pybirthdaywish.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/PyBirthdayWish-main.rar
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/PyBirthdayWish-main.zip
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pycon.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pyconi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python files.zip
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python.exe
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python_d.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python3.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python3_d.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python37.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python38.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python38.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python38_d.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/python38_d.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pythonw.exe
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pythonw.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pythonw_d.exe
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pythonw_d.pdb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pytricks.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/pywhatkit_dbs.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/quadratic.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/quiz.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/r.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/radix sort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/radix2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rahim.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rahul.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/RAJA RANNI.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/raja.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ram.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ramaya2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ramya.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ramya_.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ramya3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/readme.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/registration.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/regx.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/repeatedString.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/reverse of index.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/reverse of int.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/reverse of the string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/reverse string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/row a.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/row echolean 4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/row echolen 3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/row echolen form 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/row echolen form.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rowa1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rr.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rref 1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rs.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/rs1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/runpy.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/s.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/s1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/s3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/s4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sakila.db
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sales_by_mathes.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sales_data.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sample.mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sample1.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sangamithrai.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/save the prisoners.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sawayam1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/scon.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Scotland.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/screenshot.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/search in rotated array.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/selection s.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/selection sort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sengathir.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sengu_project.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set 1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set add.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set f1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set f2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set final.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set func.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set mutation.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set n.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/set.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/setMutation.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/shape_predictor_68_face_landmarks.dat
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/shell_sort.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/shell_sortC.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sherlock.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/shutdown.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/si.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/simarray.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/siva 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/siva.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/siva2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sivasuriyan.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/SPACE INVADERS.zip
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/space_invaders.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/speech to text.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/speech.mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Spi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 294.1.1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 295.1.2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 296.1.3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 296.2.4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 296.3.4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 297.1.5.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 297.2.6.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 298.1.7.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 298.2.8.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 299.1.9.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 299.2.10.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 300.1.11.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 300.2.12.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 301.2.13.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 302.1.14.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 302.2.15.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 303.1.16.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 303.2.17.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/SQL 303.2.18.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 304.1.18.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/SQL 304.2.18.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/SQL 305.1.19.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 305.2.20.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 306.21.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 307.22.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 308.23.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sql 309.24.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sr.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/srini.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/srini1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ss.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sss.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/stack.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/star.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/store bill.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/stp1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/string conc.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/string errors and the string lines.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/string foramting.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/string foramtomg.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/string_fromating.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/su.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/suba.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subline.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subset.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/substring.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/suck.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/suck1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sufa.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sui.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sul.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sulaiman.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sumation of odd number.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/summa.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/summaa.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sun.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/super reduced.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/super tackle.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/swap.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sydi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/sydi1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/t.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/t1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/t2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tc2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/temperature convertor.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TEMPERATURE CONVETOR.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/text to speech.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/text.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/THE Boom   Sound Effect(MP3_160K).mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/the chamber of python.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/the time in words.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/time to run.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/time_convertion.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND ADJ FOR 3X3 MATRIX.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND MATRIX MULTIPLICATION FOR 3X3 MATRIX.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND ROW ECHOLEN FORM 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND ROW ECHOLEN FORM 3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE ADJ FOR 2X2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE DETERMENET FOR 3X3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE DETERMINENT FOR 2X2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE MATRIX BY ROW COLUMN BY MATRIX INVERSTION METHOD.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE ROW ECHOLEN FORM.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE VARIABLES XY  BY MATRIX INVERSION METHOD FOR 2X2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE VARIABLES XYZ BY MATRIX INVERSION METHOD.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE VARIABLES XYZ BY MATRIX INVERSION METHOD1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO FIND THE VARIABLES XYZ BY MATRIX INVERSION METHOD2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/TO SHOW THE MARKS IN LIST.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/track mobile.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/trainee.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/traineeOxygenlevel.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/travelling.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/trig.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/try.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/trya.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tu.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/turtle 1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/turtle alt.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut 3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut eg 1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut eg 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut eg1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut eg3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut name.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut squ.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/tut.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Tutorial.ipynb
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/two char.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/two characters.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/two strings.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/u.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/u1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/up.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/user.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/users.json
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/utopiaTree.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/v.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vara1.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vara2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vara3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vara4.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/VC_redist.x64.exe
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vcamp140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vccorlib140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vcomp140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vcruntime140.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vcruntime140_1.dll
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vid_2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/video_20210222_230257.mp4
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/video_20210222_231739.mp4
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/video_player.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vidToAud.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/virtual_mouse.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/virus 3.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/virus.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/virus_outbreak.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/virus2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/voice.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/vowel substring.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/wake_up.mp3
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Wales.csv
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/weighted uniform string 2.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/weighted uniform string.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Whatsapp blast.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/WhatsApp Chat with Jothikka Poornima Ckcet.txt
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/whatsapp message.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/whatsapp.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Whatsapp_blast.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/whatsapp_emoji.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/wherearenow.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/while.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/wi-fi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/word order.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/yi.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/youtube.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/z.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/இனிய தமிழ் புத்தாண்டு நல்வாழ்த்துக்கள்.py
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/__pycache__
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Air-Canvas-project-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/bin
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Birthday-Wish-Using-Python-main
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/C
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/code
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/control-brightness-with-hand-gesture-master
C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/Desktop'''
a=a.replace('\n',',')
d=a.split(',')
for i in d:
    os.system('copy {} D:/PYTHON'.format(i))
#os.system('date')
