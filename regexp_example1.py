
txt = "201901 Dost thou love life? Then do not squander time, for that is the stuff life is made of. (Benjamin Franklin) 그대는 인생을 사랑하는가? 그렇다면 시간을 낭비하지 말라, 시간이야말로 인생을 형성하는 재료이기 때문이다. (벤자민 프랭클린) 201902 Life is like riding a bicycle. To keep your balance you must keep moving. (Albert Einstein) 인생은 자전거를 타는 것과 같다. 균형을 잡으려면 움직여야 한다. (알버트 아인슈타인) 201903 Life is a tragedy when seen in close-up, but a comedy in long-shot. (Charlie Chaplin) 인생은 가까이서 보면 비극이지만 멀리서 보면 희극이다 (찰리 채플린) 201904 Dream as if you'll live forever. Live as if you'll die today. (James Dean) 영원히 살 것처럼 꿈꾸고 오늘 죽을 것처럼 살아라. (제임스 딘) 201905 Life is an endless series of trainwrecks with only brief commercial like breaks of happiness. (Deadpool) 인생이란 괴로움의 연속이고, 행복은 광고처럼 짧다. (데드풀)"

rt = re.search("Life.*", txt)
rt. group()

rt2 = re.compile("Life.*")
rt2.findall(txt)