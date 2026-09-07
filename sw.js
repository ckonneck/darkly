self.addEventListener('fetch', e => {
  if (e.request.url.includes('.well-known/appspecific/com.chrome.devtools.json')) {
    e.respondWith(new Response(JSON.stringify({
      workspace: { root: '/opt/pocketbase', uuid: 'deadbeef-dead-beef-dead-beefdeadbeef' }
    }), { headers: { 'Content-Type': 'application/json' }}));
  }
});
