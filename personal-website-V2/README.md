# Favian Flores Developer Blog

The start of my entrepeneurial journey.

## Dependencies

- Hugo Extended 0.111.3
- ImageMagick 7.1.1
- Mria Theme 1.0.1

## Development

- Set development options in config/_default
- Run `hugo server`
- View in browser at http://localhost:1313/

## Deployment

- Configure production options in config/production
- Development options are overwritten by production, no need to set them twice
- Run `hugo` to build
- Run `hugo deploy --dryRun` to confirm which files will be changed
- Run `hugo deploy` to deploy

## Theme Documentation

- Documentation and an unmodified copy of the Mria theme can be found in the mria folder.

## Image Optimization

- Every original image should be stored in assets/images and should be optimized using the following Image Magick command
  - mogrify -strip -format webp -define webp:lossless=false -resize 1560\> -quality 82 {filename}
- Optimized images go in static/images

## Tags

- Do not use periods in tags, either exclude them or use 'dot'
- Capitalize tags in front matter, for page title
- Override tag title spellings as needed using tags folder by adding a title front matter
