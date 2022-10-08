<div align="center">

# 줄기 게임!

![Imgur](https://i.imgur.com/mz5zNOPm.png)

안녕 난 줄기야!

</div>

## Q. 뭐하는 곳이야?

A. 줄기 게임을 할 수 있어!

## Q. 어떻게 해?

A. 일단 설치부터 해!

```bash
pip install julgi-game
```

그 다음에서 터미널에서 싸우거나

```bash
julgi 줄기 빙수
```

```bash
줄기 게임! '줄기' vs '빙수'
버전: 0.1.0, 시드: 2E3D6555

[줄기] HP: 14177 / 공격력: 2864 / 마력: 2280 / 스피드: 2480 / 명중: 73 / 극대: 17
[빙수] HP: 7245 / 공격력: 1521 / 마력: 1453 / 스피드: 2497 / 명중: 76 / 극대: 15

[빙수]의 공격! 치명타! [줄기]에게 2444!의 피해를 입혔다! (남은 HP: 11733/14177)
[줄기]의 공격! [빙수]에게 2882의 피해를 입혔다! (남은 HP: 4363/7245)
[빙수]의 공격! [줄기]에게 1549의 피해를 입혔다! (남은 HP: 10184/14177)
[줄기]는 '빠르게 때리기'를 사용! 그러나 [빙수]는 회피했다!
[빙수]의 공격! 치명타! [줄기]에게 2080!의 피해를 입혔다! (남은 HP: 8104/14177)
[줄기]의 공격! 그러나 [빙수]는 회피했다!
[빙수]의 공격! 그러나 [줄기]는 회피했다!
[줄기]의 공격! [빙수]에게 3144의 피해를 입혔다! (남은 HP: 1219/7245)
[빙수]는 '두 번 베기'를 사용! [줄기]에게 1946의 피해를 입혔다! (남은 HP: 6158/14177)
[줄기]는 '참수'를 사용! 그러나 [빙수]는 회피했다!
[빙수]의 공격! [줄기]에게 1507의 피해를 입혔다! (남은 HP: 4651/14177)
[줄기]의 공격! [빙수]에게 3112의 피해를 입혔다! (남은 HP: 0/7245)

[줄기] 승! (12턴)
```

직접 함수를 불러와서 싸워!

```python
>>> from julgi import game

>>> print(game("줄기", "빙수", return_as_list=False))
줄기 게임! '줄기' vs '빙수'
버전: 0.1.0, 시드: DF9E4AA8

[줄기] HP: 14177 / 공격력: 2864 / 마력: 2280 / 스피드: 2480 / 명중: 73 / 극대: 17
[빙수] HP: 7245 / 공격력: 1521 / 마력: 1453 / 스피드: 2497 / 명중: 76 / 극대: 15

[빙수]의 공격! [줄기]에게 1607의 피해를 입혔다! (남은 HP: 12570/14177)
[줄기]의 공격! [빙수]에게 2806의 피해를 입혔다! (남은 HP: 4439/7245)
[빙수]의 공격! 치명타! [줄기]에게 2278!의 피해를 입혔다! (남은 HP: 10292/14177)
[줄기]의 공격! 치명타! [빙수]에게 4136!의 피해를 입혔다! (남은 HP: 303/7245)
[빙수]의 공격! [줄기]에게 1395의 피해를 입혔다! (남은 HP: 8897/14177)
[줄기]의 공격! [빙수]에게 2630의 피해를 입혔다! (남은 HP: 0/7245)

[줄기] 승! (6턴)
```

### 줄기야 인간적으로 너 너무 쌘거 아니냐?

난 잘 몰?루

## Q. 처음 보는 라이센스인데?

A. 줄기 라이센스야!

## A. 스킬 왜이리 적냐

Q. 미안 내가 아이디어가 부족해서...
