// Service Worker for Gym Workout Generator
// This file runs in the background and caches files for offline use

// Give our cache a name and version (change version to update cache)
const CACHE_NAME = 'workout-generator-v1';

// List of files to cache when the service worker installs
const FILES_TO_CACHE = [
  '/',
  '/static/css/style.css',
  '/static/js/app.js',
  '/manifest.json'
];

// INSTALL EVENT: Runs when the service worker is first installed
// This is where we cache our files
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Service Worker: Caching files');
        return cache.addAll(FILES_TO_CACHE);
      })
  );
});

// ACTIVATE EVENT: Runs when the service worker takes control
// This is where we clean up old caches
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activated');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          // Delete old caches that don't match our current version
          if (cache !== CACHE_NAME) {
            console.log('Service Worker: Clearing old cache');
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

// FETCH EVENT: Runs every time the browser requests a file
// We check the cache first, then fall back to the network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        // If we have it cached, return the cached version
        if (cachedResponse) {
          return cachedResponse;
        }
        // Otherwise, fetch from the network
        return fetch(event.request);
      })
  );
});
