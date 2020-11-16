const gulp = require('gulp'),
      imagemin = require('gulp-imagemin'),
      pngquant = require('imagemin-pngquant'),
      mozjpeg = require('imagemin-mozjpeg'),
      changed = require('gulp-changed'),
      notify = require('gulp-notify');

/**
 *
 * ディレクトリ
 * 
 */
const paths = {
  image_compression: {
    dist: './dist',
    src: './src',
  }
}

/**
 *
 * Compress and save the image.
 *
 * 画像を圧縮して保存。
 *
 */
gulp.task('images', () => {
  return gulp.src(paths.image_compression.src + '/**/*.{png,jpg,gif,svg}')
    .pipe(changed(paths.image_compression.dist))  // src と dist を比較して異なるものだけ処理
    .pipe(imagemin([
      pngquant({
        quality: '65-80',  // 画質
        speed: 1,  // 最低のスピード
        floyd: 0,  // ディザリングなし
      }),
      mozjpeg({
        quality: 85, // 画質
        progressive: true
      }),
      imagemin.svgo(),
      imagemin.optipng(),
      imagemin.gifsicle()
    ]))
    .pipe(gulp.dest(distDir))  // 保存
    .pipe(notify('&#x1f363; images task finished &#x1f363;'));
});