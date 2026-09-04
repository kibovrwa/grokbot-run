const CANONICAL_HOST = "grokbot.run";
const ASSET_EXT = /\.(png|svg|xml|txt|ico|css|js|json|webp|jpe?g|gif|woff2?|map)$/i;

function normalizePath(pathname) {
  if (pathname === "/index.html") return "/";
  if (pathname.endsWith("/index.html")) {
    return pathname.slice(0, -"index.html".length);
  }
  if (pathname !== "/" && !pathname.endsWith("/") && !ASSET_EXT.test(pathname)) {
    return pathname + "/";
  }
  return pathname;
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname.toLowerCase();

  if (host.endsWith(".pages.dev")) {
    const res = await context.next();
    const headers = new Headers(res.headers);
    headers.set("X-Robots-Tag", "noindex, nofollow");
    return new Response(res.body, {
      status: res.status,
      statusText: res.statusText,
      headers,
    });
  }

  const dest = new URL(url);
  let changed = false;

  if (host === "www.grokbot.run") {
    dest.hostname = CANONICAL_HOST;
    dest.protocol = "https:";
    changed = true;
  } else if (host === CANONICAL_HOST && dest.protocol === "http:") {
    dest.protocol = "https:";
    changed = true;
  }

  const nextPath = normalizePath(dest.pathname);
  if (nextPath !== dest.pathname) {
    dest.pathname = nextPath;
    changed = true;
  }

  if (changed) {
    return Response.redirect(dest.toString(), 301);
  }

  return context.next();
}
