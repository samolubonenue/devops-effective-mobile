FROM python:3.12-alpine

LABEL maintainer="Effective Mobile Test Task"
LABEL description="Simple Python HTTP server"

WORKDIR /app

RUN addgroup -g 1000 appgroup && \
    adduser -u 1000 -G appgroup -D appuser

COPY --chown=appuser:appgroup app.py .

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

CMD ["python", "app.py"]
