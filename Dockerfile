FROM python:3.8-slim

# 환경 변수 설정
ENV APP_HOME /app
ENV PORT 8000
ENV HOST 0.0.0.0
ENV TZ=Asia/Seoul
ENV LC_ALL=C.UTF-8

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 빌드한 디렉토리의 모든 파일을 컨테이너 안의 WORKDIR 경로로 복사
COPY . $APP_HOME

EXPOSE 8000

# 실행
CMD ["python","app.py"]