'''
그래프는 아이템(사물 또는 추상적 개념)들과 이들사이의 연결관계를 표현한다.

그래프는 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료구조
V : 정점의 갯수, E : 그래프에 포함된 간선의 갯수
V개의 정점을 가지는 그래프는 최대 abs(V)*(abs(V)-1)/2 개의 간선이 가능
예) 5개의 정점의 최개 간선수는 10개

그래프는 선형자료구조나 트리 자료구조로 표현하기
어려운 N:N관계를 가지는 원소들을 표현하기에 용이하다.


그래프를 만들때 일반적으로
인접행렬과 인접리스트를 사용
인접행렬 :
V*V크기의 2차원 배열을 이용해서 간선정보를 저장

인접리스트 :
각 정점마다 해당 정점으로 나가는 간선의 정보를 저장

그래프의 단점:
정점의 갯수가 많을수록 행렬의 크기가 커져서 메모리가 커진다.
이를 해결하기 위해 하나의 정점의 대한 인접정점들을 각각 노드로 연결하는 연결리스트로 저장

0       <<<6, 5, 1, 2
1       <<<5, 4
2       <<< 0
3       <<< 4
4       <<< 3, 0, 4
5
'''

'''
다음은 연결되어있는 두개의 점점사이에 간선을 순서대로 연결해놓은것이다.
모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오
시작은 정점 1로 시작하자
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
# 정점수, 간선수
V, E = map(int, input().split())
# 빈리스트 생성 1~V까지 사용하기 때문에 V+1개를 생성
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
print(G)
for i in range(1,V+1):
    print(i, G[i])