from presidio_analyzer import RecognizerResult

class PostProcessor:
    def __init__(self, score_threshold: float = 0.0):
        self.score_threshold = score_threshold

    def resolve_overlaps(self, results: list[RecognizerResult]) -> list[RecognizerResult]:
        # Skor eşik altındakileri filtrele
        filtered = [r for r in results if r.score >= self.score_threshold]

        # Skora göre sırala
        filtered = sorted(filtered, key=lambda r: (-r.score, r.start, -r.end))

        final = []
        for res in filtered:
            if not any(
                res.start < r.end and res.end > r.start
                for r in final
            ):
                final.append(res)

        return final
