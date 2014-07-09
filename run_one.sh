DATAPATH=/search/zf/bh1/data
city=`echo $1 | python url_encode.py`
url="http://www.daodao.com/Search?q=$city" 
#COOKIE_DATA=cookie
#wget --load-cookies=$COOKIE_DATA --save-cookies=$COOKIE_DATA --keep-session-cookies $url -O $DATAPATH/$city -U "Chrome/32.0.1700.102 Safari/537.36"

sh /search/zf/proxy/wget.sh $url $DATAPATH/$city

python get_jingdian.py $DATAPATH/$city $city > $DATAPATH/$city.jingdian
python get_jiudian.py $DATAPATH/$city $city > $DATAPATH/$city.jiudian
python get_canguan.py $DATAPATH/$city $city > $DATAPATH/$city.canguan
