# auto-generated: docs-exclude
"""datago.ocean_buoy 예제 — 해양관측부이 최신 관측데이터.

실행 모드:
- ``KPUBDATA_MODE=replay`` — fixture 재생(키 불필요) / 미지정 — 실호출
- 파라미터는 spec의 예제 ``buoy_0089``와 동일(replay 매칭 계약)
"""

from __future__ import annotations

import os

from kpubdata import Client


def main() -> None:
    """datago.ocean_buoy 기본 조회를 실행한다."""
    api_key = os.environ.get("KPUBDATA_DATAGO_API_KEY", "replay-mode")
    client = Client(provider_keys={"datago": api_key}, cache=False)

    dataset = client.dataset("datago.ocean_buoy")
    batch = dataset.list(obsCode="TW_0089", page=1, page_size=10)

    # 구조 검증: envelope 계약(총건수 보고) + 레코드 형태
    assert batch.total_count is not None, "totalCount가 보고되어야 한다"
    assert isinstance(batch.items, list), "items는 리스트여야 한다"
    assert all(isinstance(item, dict) for item in batch.items), "레코드는 dict여야 한다"

    print(f"datago.ocean_buoy: {len(batch.items)}건 / 전체 {batch.total_count}건")


if __name__ == "__main__":
    main()
