ó
 ’c           @   s  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z e d d  Z e Z e j GHe j d  d e j k rTd e j k r?d	 GHqTd
 GHe j j   n  e e  e j d  e j   Z e j e   e j e j  j!   d d d g e _" d   Z d   Z# d   Z$ d   Z% d Z& d  Z' g  Z( d   Z) d   Z* e+ d k r
e)   n  d S(   i    i’’’’N(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   profisor_token.pyt   rt   cleart   GOODs'   Nawe Fileaka bgora ba profisor_token.pyt   utf8t   max_timei   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   280201040o.pyR
      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   280201040o.pyt   acak!   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR	   t   stdoutt   write(   R   R   R   t   jR   (    (    s   280201040o.pyR   )   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gøėQø?(   R	   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   280201040o.pyt   hamza3   s    s  
============================================#Profisor#================================================
Chanell : CrackerForKurd0
Me Tele : Profis0r
Crator  : Profis0r
============================================#Profisor#================================================
c          C   s  t  j d  t  j d  t GHHHt d  }  |  j d d  } t d  } t j d | d | d	  } t j |  } d
 | k rĖ t d d  } | j	 | d
  | j
   d GHt j d  t   nE d | d k r÷ d GHt j d  t   n d GHt j d  t   d  S(   NR   s   rm -rif token.txts   Number/Email : t    R   s   Password : s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens	   token.txtR   s   
 Awa Tokenakata gÉ?s   www.facebook.comt	   error_msgs   
Account Peshtr Login krawagėQøÕ?s   
[!] Number/ID/Password Xalatai   (   R   t   systemt   bannert	   raw_inputR   t   brt   opent   jsont   loadR   t   closeR   R    t
   show_tokent   login_fb(   t   iidt   idt   pwdt   dataR!   t   st(    (    s   280201040o.pyR0   D   s0    


c           C   sA   d GHd d GHHt  j d  Hd d GHt d  t  j d  d  S(   Ns    Tokenakat Copy bw la token.txti/   t   -s   cat token.txts   [Enter Bka Bo Dwbara bwnawa] s   python2 profisor_token.py(   R   R'   R)   (    (    (    s   280201040o.pyR/   _   s    		
t   __main__(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](,   t   Falset   foot   barR   R	   R   t   datetimeR   t   hashlibt   ret	   threadingR,   t   urllibt	   cookielibt   requestst	   mechanizet   multiprocessing.poolR    t   requests.exceptionsR   R   R+   t   hdt   fdt   nameR'   R
   t   reloadt   setdefaultencodingR*   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R#   R(   t   backR2   R0   R/   t   __name__(    (    (    s   280201040o.pyt   <module>   sD   

			
			
