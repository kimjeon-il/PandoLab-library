# 메모리 최종 판정

**완료: 이번 160회 연속 전환/60회 캐시 재전송 범위에서 안정성 유지.** 무기한 사용이나 다른 프로젝트 크기의 누수 부재를 확정하지 않는다.

| trace 없는 대조 | private @60 MiB | private @160 MiB | 차이 MiB | 국경 heap MiB | 메인 heap MiB |
| --- | ---: | ---: | ---: | --- | --- |
| A-untraced-memory | 1823.9 | 1831.0 | 7.1 | 101.8 → 101.8 | 120.8 → 121.0 |
| B-untraced-memory | 1857.1 | 1860.0 | 2.9 | 129.8 → 129.8 | 120.8 → 121.0 |

B의 40→160회 공유국경 heap은 129.7811MiB로 동일하고 캐시는 한 패킷, 추정 15.79MiB로 일정했다. main heap은 60→160회 약 0.233MiB 증가했다. B working set은 1659.34→1667.76MiB로 약 8.42MiB 변동했다. private는 10회 1893.41MiB의 초기 고점에서 내려와 40/60/100/160회 1855.41/1857.05/1858.60/1860.00MiB였다. A도 같은 범위의 초기 확장 후 변동을 보였다. 지속적인 캐시 개수 증가나 WASM capacity 증가는 관측되지 않았다.

trace를 켠 A/B/A2는 60→160회 native private가 약 67–71MiB 증가했지만, tracing만 제거한 대조에서는 A +7.12MiB, B +2.95MiB였다. 진단 수집의 영향을 분리할 근거이며 해당 trace 내부 allocator를 특정한 것은 아니다. 모든 JS/WASM과 private/working set의 GC 전후 원본은 memory.csv 및 memory JSON.gz에 있다.

B의 자연 경로 국경 JS heap은 A보다 약 27.9MiB 크다. 캐시 추정 15.79MiB와 실제 heap 차이는 정의가 다르다. 96MiB는 보관 packet 추정량 기준의 코드 상한이며 전체 Worker heap 상한이 아니다. 강제 재준비 시 첫 확장 뒤 국경 heap은 10→60회 162.206→162.279MiB로 약 0.073MiB 증가했고, 이때도 캐시 수/추정량은 같았다.

B 강제 60회는 전부 cache hit였으며 수신 데이터 해시와 여섯 보관 ArrayBuffer.detached=false를 확인했다. 96MiB 초과 입력에 대한 실GPU admission 거부는 미측정이다. 모든 완료 memory 실행에서 브라우저 종료 후 소유 PID가 0이었다. 장기 수시간의 여러 프로젝트 전환/전체 viewport는 후속 범위다.
