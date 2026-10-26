"""第 1 周 Python 练习：销售额汇总。

在终端运行：
    python3 exercises/week1_sales.py
"""


def summarize_sales(sales: list[float]) -> dict:
    """输入一组销售额，返回总和、成交客单价、最大值。

    客单价 = 成交金额 / 成交单数。金额为 0 的订单不计入分母。
    """
    if not sales:
        return {"sum": 0, "mean": 0, "max": 0, "paid_count": 0}

    paid = [x for x in sales if x > 50]
    total = sum(paid)
    return {
        "sum": total,
        "mean": total / len(paid) if paid else 0,
        "max": max(paid) if paid else 0,
        "paid_count": len(paid),
    }


if __name__ == "__main__":
    # 假装这是某店一周的订单金额（后面会换成 pandas 读 CSV）
    week_sales = [128.0, 56.5, 320.0, 99.9, 45.0, 210.0, 0.0]
    result = summarize_sales(week_sales)

    print("本周订单金额：", week_sales)
    print("成交单数：", result["paid_count"], "（已去掉 50 元订单）")
    print("总和：", round(result["sum"], 2))
    print("客单价（均值）：", round(result["mean"], 2))
    print("最大单：", result["max"])
    print()
    print("对比：若把 0 元也算进去，客单价会被拉低到 122.77。")
    print("联动预告：下周用 pandas 对「每月」做同样的 sum / mean。")
