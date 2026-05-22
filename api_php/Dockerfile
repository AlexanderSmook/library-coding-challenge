FROM php:8.2

WORKDIR /api

RUN apt update && apt install -y
RUN apt-get install -y \
    libzip-dev \
    zip \
    libicu-dev
RUN rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure intl && docker-php-ext-install intl

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && chmod +x /usr/bin/composer

COPY . .

RUN composer install

EXPOSE 4000

# PHP built-in web server
CMD ["php", "-S" , "0.0.0.0:4000"]
