FROM golang:latest

WORKDIR /app
COPY . .

RUN go build -o main .

EXPOSE 8090
CMD ["./main"]

