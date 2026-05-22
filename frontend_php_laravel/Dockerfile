FROM php:8.2

WORKDIR /frontend

RUN apt update && apt install -y
RUN apt-get install -y \
    libzip-dev \
    zip \
    libicu-dev
RUN rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure intl && docker-php-ext-install intl

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && chmod +x /usr/bin/composer

RUN apt-get update && apt-get install -y nodejs npm

COPY . .

RUN composer install
RUN npm install

EXPOSE 3000

CMD ["php", "artisan" , "serve", "--port=3000", "--host=0.0.0.0" ]
