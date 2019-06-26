// gulpfile.js
var gulp = require('gulp');
var tinyping = require('gulp-tinypng-compress');

gulp.task('imagemin', function () {
    gulp.src('./src/*.{png,jpg,jpeg}')
        .pipe(tinyping({
            key: '1xlxGPO6tzE49mCcx6vNFqEhRNe1iC4Z' // TinyPNGのAPI Key
        }))
        .pipe(gulp.dest('./dist'));
});

gulp.task('default', ['tinypng']);
