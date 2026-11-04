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

§0.1의 실무 선별 기준은 **실제로 달라진 연결된 구역의 면적 약 500km² 이상**이다. 그보다 작은 일반적 변화의 개별 정밀 복원은 원칙적으로 생략하되, 중요한 역사 사건·국가·도시·도서 귀속과 필요한 연결성의 예외를 유지한다. 실제 최대 확대 캡처(지도 1180×709 CSS px, DPR 1) 기반 모의 전후 비교에서 사용자가 약 500km²부터 식별된다고 판단한 데 따른 작업 우선순위다. 보편적인 최소 가시 면적·정확도 보장이 아니며, 형상·폭·표시 배율을 함께 판단하고 별도 고정 폭 기준은 두지 않는다. 자세한 조건·생략 및 보존 범위는 정본을 따르며 기존 지역 재조사·자료 삭제·핀 변경을 요구하지 않는다.
