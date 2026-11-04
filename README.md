# PandoLab library data

Storage only. No tests, validation jobs or generators run in this repository. Application tools live in [Pando](https://github.com/kimjeon-il/Pando).

- [Reports and research index](reports/README.md)
- [Compressed original evidence](archive/README.md)
- Editable library: library.json and objects/.
- Runtime baseline: assets/data/. Branches preserve paired app datasets.
- Current terrain: terrain/v0.13.3/, LOD0-5 of one dataset. Older tint/manifests remain in Git history. Pixels are unchanged.

Only terrain is published from gh-pages. Main holds the full storage corpus and is not a Pages source.

## 역사 경계 라이브러리 작업 규칙

규칙 정본은 Pando의 [역사적 국경·해안선 복원 공통 작업 규칙](https://github.com/kimjeon-il/Pando/blob/work/gis/docs/historical-border-reconstruction-policy.md)이다. 이 저장소에 별도의 경쟁 규칙을 만들지 않는다.

§0.1의 잠정 선별 기준은 **변화 면적 약 10km² 또는 의미 있는 변화 폭·경계 이동폭 약 3km**다. 일반적인 변화가 둘 다 미만이면 개별 정밀 복원을 원칙적으로 생략하되, 중요한 역사 사건·국가·도시·도서 귀속과 필요한 연결성의 예외를 유지한다. 화면 크기·형상에 따른 계산 추정이며 실제 변화 도형의 식별 실험은 미실행이다. 산정 조건·생략 및 보존 범위는 정본을 따르고, 기존 지역 재조사·자료 삭제·핀 변경을 요구하지 않는다.
