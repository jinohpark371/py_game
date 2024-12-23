# py_game

py_game 프로젝트는 블록깨기 게임을 구현한 프로젝트입니다.

##시작하기

로컬에서 run.py 파일을 실행 후 스페이스 바를 누를 시 게임이 시작됩니다. 스페이스 바를 누르게 되면 패들에 달려 있는 공이 벽돌 쪽으로 이동하면서 벽돌과 충돌할 경우 벽돌이 깨지게 되고 모든 벽돌을 깰 시 게임이 종료됩니다.

###필수 사항

[python 3.10 or 3.12]
[pygame]

###설치 방법

1.리포지토리 클론 
  
  git clone https://github.com/jinohpark371/py_game.git

2.pygame 설치(설치방법 - pip install pygame
)

##사용법과 구현원리

1.run.py파일을 실행

2.implement.py의 구현 원리

basic 클래스:
Basic 클래스는 모든 게임 오브젝트(공, 블록, 패들 등)의 기본 속성인 색상, 위치, 크기, 속도 등을 관리합니다.
move 메서드는 오브젝트가 지정된 방향(dir)으로 이동할 수 있게 합니다. dx와 dy는 이동량을 계산하여 오브젝트를 이동시킵니다.

Block 클래스:
Block 클래스는 게임에서 깨져야 하는 블록을 나타냅니다. 블록은 색상과 위치, 그리고 alive 상태를 가집니다.
draw 메서드는 블록을 화면에 그립니다. alive 상태가 True일 때만 그립니다.
collide 메서드는 블록이 특정 색상일 때 색상을 변경하거나 블록을 깨고 아이템을 생성하는 기능을 합니다. 깨진 블록이 아이템을 생성할 수 있습니다. 아이템은 'red'와 'blue'로 구분되며 각 아이템에 따라 다른 이벤트가 발생합니다.

Paddle 클래스:
Paddle 클래스는 게임의 패들을 나타냅니다. 패들은 화면에서 왼쪽과 오른쪽으로 이동할 수 있습니다.
draw 메서드는 패들을 화면에 그립니다.
move_paddle 메서드는 사용자가 좌우 화살표 키를 눌러 패들을 이동시키는 기능을 담당합니다. 

Ball 클래스:
Ball 클래스는 게임의 공을 나타냅니다. 공은 일정한 방향과 속도로 이동하며, 벽, 패들, 블록과 충돌합니다.
draw 메서드는 공을 화면에 그립니다.
collide_block 메서드는 공이 블록과 충돌했을 때의 동작을 처리합니다. 블록과의 충돌 방향에 따라 공의 방향을 변경합니다.
collide_paddle 메서드는 공이 패들과 충돌했을 때의 동작을 처리합니다.
hit_wall 메서드는 공이 벽과 충돌했을 때의 동작을 처리합니다. 좌우 벽이나 상단 벽에 충돌하면 공의 방향을 반사시킵니다.
alive 메서드는 공이 화면 아래로 떨어졌을 때 생명(life)을 감소시키고, 남은 생명이 0보다 크면 True, 그렇지 않으면 False를 반환합니다.

Item 클래스:
Item 클래스는 아이템을 나타냅니다. 아이템은 'red'와 'blue' 두 종류가 있으며, 각 아이템은 색상과 위치를 가집니다.
draw 메서드는 아이템을 화면에 그립니다.
move 메서드는 아이템을 아래로 이동시킵니다. 아이템은 주로 블록이 깨질 때 생성됩니다.

3.runpy.py의 구현원리
게임 초기화 및 설정:
pygame.init()으로 Pygame 라이브러리를 초기화하고, 게임 화면을 설정합니다.
fps_clock은 게임의 프레임 레이트를 제어하는 객체입니다.
paddle, ball1, BLOCKS, ITEMS, BALLS, life, start 변수는 각각 패들, 공, 블록, 아이템, 공 리스트, 생명 횟수, 게임 시작 상태를 관리합니다.

create_blocks() 함수:
게임 화면에 블록을 생성하는 함수입니다. 

tick() 함수:
게임의 주요 로직을 처리하는 함수입니다.
이벤트 처리: 사용자 입력을 처리합니다.
pygame.KEYDOWN: K_ESCAPE는 게임을 종료하고, K_SPACE는 게임을 시작합니다.
paddle.move_paddle(event)로 패들이 좌우로 이동합니다.

공 이동 및 충돌 처리:
게임이 시작되면 공(ball)을 이동시키고, 블록과 충돌 시 블록을 깨며 아이템을 생성합니다.
공과 패들, 벽의 충돌을 처리합니다.
공이 화면 아래로 떨어지면 life를 감소시키고, 생명이 0이면 게임 오버 상태로 전환됩니다.

아이템 이동 및 충돌 처리:
아이템은 패들과 충돌 시, 아이템 종류에 따라 점수 증가(red) 또는 공 복제(blue) 효과를 발생시킵니다


main() 함수:
블록 및 아이템 그리기: create_blocks()로 블록을 생성하고, 게임 화면에 각 객체(패들, 블록, 아이템, 공)를 그립니다.
점수 및 생명 표시: 점수는 남은 블록 수에 따라 계산되고, 생명은 life 변수로 표시됩니다.
게임 오버시 "Game Over!"표시하며 모든 블록을 다 부순경우  "Cleared!"를 표시합니다.


