/*
 Highcharts JS v10.2.1 (2022-08-29)

 (c) 2016-2021 Highsoft AS
 Authors: Jon Arild Nygard

 License: www.highcharts.com/license
*/
(function(b){"object"===typeof module&&module.exports?(b["default"]=b,module.exports=b):"function"===typeof define&&define.amd?define("highcharts/modules/wordcloud",["highcharts"],function(h){b(h);b.Highcharts=h;return b}):b("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(b){function h(b,g,k,l){b.hasOwnProperty(g)||(b[g]=l.apply(null,k),"function"===typeof CustomEvent&&window.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:g,module:b[g]}})))}b=b?b._modules:{};h(b,
"Series/DrawPointUtilities.js",[b["Core/Utilities.js"]],function(b){function g(b){switch(b.series&&b.series.type){case "treemap":return k(b.plotY)&&null!==b.y;default:return!b.isNull}}var k=b.isNumber;return{draw:function(b,e){var n=e.animatableAttribs,f=e.onComplete,l=e.css,q=e.renderer,k=b.series&&b.series.chart.hasRendered?void 0:b.series&&b.series.options.animation,p=b.graphic;e.attribs=e.attribs||{};e.attribs["class"]=b.getClassName();if(g(b))p||(b.graphic=p="text"===e.shapeType?q.text():q[e.shapeType](e.shapeArgs||
{}),p.add(e.group)),l&&p.css(l),p.attr(e.attribs).animate(n,e.isNew?!1:k,f);else if(p){var h=function(){b.graphic=p=p&&p.destroy();"function"===typeof f&&f()};Object.keys(n).length?p.animate(n,void 0,function(){return h()}):h()}},shouldDraw:g}});h(b,"Series/Wordcloud/WordcloudPoint.js",[b["Core/Series/SeriesRegistry.js"],b["Core/Utilities.js"]],function(b,g){var k=this&&this.__extends||function(){var b=function(e,n){b=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(b,e){b.__proto__=
e}||function(b,e){for(var f in e)e.hasOwnProperty(f)&&(b[f]=e[f])};return b(e,n)};return function(e,n){function f(){this.constructor=e}b(e,n);e.prototype=null===n?Object.create(n):(f.prototype=n.prototype,new f)}}();g=g.extend;b=function(b){function e(){var e=null!==b&&b.apply(this,arguments)||this;e.dimensions=void 0;e.options=void 0;e.polygon=void 0;e.rect=void 0;e.series=void 0;return e}k(e,b);e.prototype.isValid=function(){return!0};return e}(b.seriesTypes.column.prototype.pointClass);g(b.prototype,
{weight:1});return b});h(b,"Series/Wordcloud/WordcloudUtils.js",[b["Core/Globals.js"],b["Core/Utilities.js"]],function(b,g){function k(a,c){return!(c.left>a.right||c.right<a.left||c.top>a.bottom||c.bottom<a.top)}function h(a,c){var d=c[0]-a[0];a=c[1]-a[1];return[[-a,d],[a,-d]]}function e(a){var c=a.axes||[];if(!c.length){c=[];var d=d=a.concat([a[0]]);d.reduce(function(a,d){var b=h(a,d)[0];A(c,function(a){return a[0]===b[0]&&a[1]===b[1]})||c.push(b);return d});a.axes=c}return c}function n(a,c){a=a.map(function(a){return a[0]*
c[0]+a[1]*c[1]});return{min:Math.min.apply(this,a),max:Math.max.apply(this,a)}}function f(a,c){var d=e(a),b=e(c);d=d.concat(b);return!A(d,function(d){var b=n(a,d);d=n(c,d);return!!(d.min>b.max||d.max<b.min)})}function H(a,c){var d=!1,b=a.rect,e=a.polygon,x=a.lastCollidedWith,g=function(c){var d=k(b,c.rect);d&&(a.rotation%90||c.rotation%90)&&(d=f(e,c.polygon));return d};x&&((d=g(x))||delete a.lastCollidedWith);d||(d=!!A(c,function(c){var d=g(c);d&&(a.lastCollidedWith=c);return d}));return d}function q(a,
c){c=4*a;var d=Math.ceil((Math.sqrt(c)-1)/2),b=2*d+1,e=Math.pow(b,2),f=!1;--b;1E4>=a&&("boolean"===typeof f&&c>=e-b&&(f={x:d-(e-c),y:-d}),e-=b,"boolean"===typeof f&&c>=e-b&&(f={x:-d,y:-d+(e-c)}),e-=b,"boolean"===typeof f&&(f=c>=e-b?{x:-d+(e-c),y:d}:{x:d,y:d-(e-c-b)}),f.x*=5,f.y*=5);return f}function t(a,c){var d=c.width/2,b=-(c.height/2),e=c.height/2;return!(-(c.width/2)<a.left&&d>a.right&&b<a.top&&e>a.bottom)}function p(a,c,d){return d.map(function(d){return[d[0]+a,d[1]+c]})}function w(a,c){c=m(c)?
c:14;c=Math.pow(10,c);return Math.round(a*c)/c}function v(a,c){var d=a[0];a=a[1];var b=y*-c;c=Math.cos(b);b=Math.sin(b);return[w(d*c-a*b),w(d*b+a*c)]}function B(a,c,d){a=v([a[0]-c[0],a[1]-c[1]],d);return[a[0]+c[0],a[1]+c[1]]}var y=b.deg2rad,D=g.extend,A=g.find,m=g.isNumber,C=g.isObject,z=g.merge;return{archimedeanSpiral:function(a,c){var d=c.field;c=!1;d=d.width*d.width+d.height*d.height;var b=.8*a;1E4>=a&&(c={x:b*Math.cos(b),y:b*Math.sin(b)},Math.min(Math.abs(c.x),Math.abs(c.y))<d||(c=!1));return c},
extendPlayingField:function(a,c){if(C(a)&&C(c)){var d=c.bottom-c.top;var b=c.right-c.left;c=a.ratioX;var e=a.ratioY;d=b*c>d*e?b:d;a=z(a,{width:a.width+d*c*2,height:a.height+d*e*2})}return a},getBoundingBoxFromPolygon:function(a){return a.reduce(function(a,d){var c=d[0];d=d[1];a.left=Math.min(c,a.left);a.right=Math.max(c,a.right);a.bottom=Math.max(d,a.bottom);a.top=Math.min(d,a.top);return a},{left:Number.MAX_VALUE,right:-Number.MAX_VALUE,bottom:-Number.MAX_VALUE,top:Number.MAX_VALUE})},getPlayingField:function(a,
c,d){d=d.reduce(function(a,c){c=c.dimensions;var b=Math.max(c.width,c.height);a.maxHeight=Math.max(a.maxHeight,c.height);a.maxWidth=Math.max(a.maxWidth,c.width);a.area+=b*b;return a},{maxHeight:0,maxWidth:0,area:0});d=Math.max(d.maxHeight,d.maxWidth,.85*Math.sqrt(d.area));var b=a>c?a/c:1;a=c>a?c/a:1;return{width:d*b,height:d*a,ratioX:b,ratioY:a}},getPolygon:function(a,c,b,e,f){var d=[a,c],g=a-b/2;a+=b/2;b=c-e/2;c+=e/2;return[[g,b],[a,b],[a,c],[g,c]].map(function(a){return B(a,d,-f)})},getRandomPosition:function(a){return Math.round(a*
(Math.random()+.5)/2)},getRotation:function(a,c,b,e){var d=!1;m(a)&&m(c)&&m(b)&&m(e)&&0<a&&-1<c&&e>b&&(d=b+c%a*((e-b)/(a-1||1)));return d},getScale:function(a,c,b){var d=2*Math.max(Math.abs(b.top),Math.abs(b.bottom));b=2*Math.max(Math.abs(b.left),Math.abs(b.right));return Math.min(0<b?1/b*a:1,0<d?1/d*c:1)},getSpiral:function(a,c){var b,e=[];for(b=1;1E4>b;b++)e.push(a(b,c));return function(a){return 1E4>=a?e[a-1]:!1}},intersectionTesting:function(a,b){var c=b.placed,e=b.field,f=b.rectangle,g=b.polygon,
n=b.spiral,h=1,k={x:0,y:0},m=a.rect=D({},f);a.polygon=g;for(a.rotation=b.rotation;!1!==k&&(H(a,c)||t(m,e));)k=n(h),C(k)&&(m.left=f.left+k.x,m.right=f.right+k.x,m.top=f.top+k.y,m.bottom=f.bottom+k.y,a.polygon=p(k.x,k.y,g)),h++;return k},isPolygonsColliding:f,isRectanglesIntersecting:k,rectangularSpiral:function(a,b){a=q(a,b);b=b.field;a&&(a.x*=b.ratioX,a.y*=b.ratioY);return a},rotate2DToOrigin:v,rotate2DToPoint:B,squareSpiral:q,updateFieldBoundaries:function(a,b){if(!m(a.left)||a.left>b.left)a.left=
b.left;if(!m(a.right)||a.right<b.right)a.right=b.right;if(!m(a.top)||a.top>b.top)a.top=b.top;if(!m(a.bottom)||a.bottom<b.bottom)a.bottom=b.bottom;return a}}});h(b,"Series/Wordcloud/WordcloudSeries.js",[b["Series/DrawPointUtilities.js"],b["Core/Globals.js"],b["Core/Series/Series.js"],b["Core/Series/SeriesRegistry.js"],b["Core/Utilities.js"],b["Series/Wordcloud/WordcloudPoint.js"],b["Series/Wordcloud/WordcloudUtils.js"]],function(b,g,k,h,e,n,f){var l=this&&this.__extends||function(){var b=function(a,
c){b=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(b,a){b.__proto__=a}||function(b,a){for(var c in a)a.hasOwnProperty(c)&&(b[c]=a[c])};return b(a,c)};return function(a,c){function d(){this.constructor=a}b(a,c);a.prototype=null===c?Object.create(c):(d.prototype=c.prototype,new d)}}(),q=g.noop,t=h.seriesTypes.column,p=e.extend,w=e.isArray,v=e.isNumber,B=e.isObject,y=e.merge;e=f.archimedeanSpiral;var D=f.extendPlayingField,A=f.getBoundingBoxFromPolygon,m=f.getPlayingField,C=f.getPolygon,
z=f.getRandomPosition,a=f.getRotation,c=f.getScale,d=f.getSpiral,F=f.intersectionTesting,I=f.isPolygonsColliding,x=f.rectangularSpiral,J=f.rotate2DToOrigin,K=f.rotate2DToPoint,L=f.squareSpiral,M=f.updateFieldBoundaries;f=function(a){function e(){var b=null!==a&&a.apply(this,arguments)||this;b.data=void 0;b.options=void 0;b.points=void 0;return b}l(e,a);e.prototype.bindAxes=function(){var a={endOnTick:!1,gridLineWidth:0,lineWidth:0,maxPadding:0,startOnTick:!1,title:void 0,tickPositions:[]};k.prototype.bindAxes.call(this);
p(this.yAxis.options,a);p(this.xAxis.options,a)};e.prototype.pointAttribs=function(a,b){a=g.seriesTypes.column.prototype.pointAttribs.call(this,a,b);delete a.stroke;delete a["stroke-width"];return a};e.prototype.deriveFontSize=function(a,b,c){a=v(a)?a:0;b=v(b)?b:1;c=v(c)?c:1;return Math.floor(Math.max(c,a*b))};e.prototype.drawPoints=function(){var a=this,e=a.hasRendered,f=a.xAxis,g=a.yAxis,k=a.group,h=a.options,n=h.animation,N=h.allowExtendPlayingField,q=a.chart.renderer,l=q.text().add(k),t=[],w=
a.placementStrategy[h.placementStrategy],x=h.rotation,z=a.points.map(function(a){return a.weight}),y=Math.max.apply(null,z),E=a.points.concat().sort(function(a,b){return b.weight-a.weight});a.group.attr({scaleX:1,scaleY:1});E.forEach(function(b){var c=a.deriveFontSize(1/y*b.weight,h.maxFontSize,h.minFontSize);c=p({fontSize:c+"px"},h.style);l.css(c).attr({x:0,y:0,text:b.name});c=l.getBBox(!0);b.dimensions={height:c.height,width:c.width}});var u=m(f.len,g.len,E);var G=d(a.spirals[h.spiral],{field:u});
E.forEach(function(c){var d=a.deriveFontSize(1/y*c.weight,h.maxFontSize,h.minFontSize);d=p({fontSize:d+"px"},h.style);var f=w(c,{data:E,field:u,placed:t,rotation:x}),g=p(a.pointAttribs(c,c.selected&&"select"),{align:"center","alignment-baseline":"middle","dominant-baseline":"middle",x:f.x,y:f.y,text:c.name,rotation:v(f.rotation)?f.rotation:void 0}),m=C(f.x,f.y,c.dimensions.width,c.dimensions.height,f.rotation),r=A(m),l=F(c,{rectangle:r,polygon:m,field:u,placed:t,spiral:G,rotation:f.rotation});!l&&
N&&(u=D(u,r),l=F(c,{rectangle:r,polygon:m,field:u,placed:t,spiral:G,rotation:f.rotation}));B(l)?(g.x=(g.x||0)+l.x,g.y=(g.y||0)+l.y,r.left+=l.x,r.right+=l.x,r.top+=l.y,r.bottom+=l.y,u=M(u,r),t.push(c),c.isNull=!1,c.isInside=!0):c.isNull=!0;if(n){var O={x:g.x,y:g.y};e?(delete g.x,delete g.y):(g.x=0,g.y=0)}b.draw(c,{animatableAttribs:O,attribs:g,css:d,group:k,renderer:q,shapeArgs:void 0,shapeType:"text"})});l=l.destroy();f=c(f.len,g.len,u);a.group.attr({scaleX:f,scaleY:f})};e.prototype.hasData=function(){return B(this)&&
!0===this.visible&&w(this.points)&&0<this.points.length};e.prototype.getPlotBox=function(){var a=this.chart,b=a.inverted,c=this[b?"yAxis":"xAxis"];b=this[b?"xAxis":"yAxis"];return{translateX:(c?c.left:a.plotLeft)+(c?c.len:a.plotWidth)/2,translateY:(b?b.top:a.plotTop)+(b?b.len:a.plotHeight)/2,scaleX:1,scaleY:1}};e.defaultOptions=y(t.defaultOptions,{allowExtendPlayingField:!0,animation:{duration:500},borderWidth:0,clip:!1,colorByPoint:!0,cropThreshold:Infinity,minFontSize:1,maxFontSize:25,placementStrategy:"center",
rotation:{from:0,orientations:2,to:90},showInLegend:!1,spiral:"rectangular",style:{fontFamily:"sans-serif",fontWeight:"900",whiteSpace:"nowrap"},tooltip:{followPointer:!0,pointFormat:'<span style="color:{point.color}">\u25cf</span> {series.name}: <b>{point.weight}</b><br/>'}});return e}(t);p(f.prototype,{animate:q,animateDrilldown:q,animateDrillupFrom:q,pointClass:n,setClip:q,placementStrategy:{random:function(b,c){var d=c.field;c=c.rotation;return{x:z(d.width)-d.width/2,y:z(d.height)-d.height/2,
rotation:a(c.orientations,b.index,c.from,c.to)}},center:function(b,c){c=c.rotation;return{x:0,y:0,rotation:a(c.orientations,b.index,c.from,c.to)}}},pointArrayMap:["weight"],spirals:{archimedean:e,rectangular:x,square:L},utils:{extendPlayingField:D,getRotation:a,isPolygonsColliding:I,rotate2DToOrigin:J,rotate2DToPoint:K}});h.registerSeriesType("wordcloud",f);"";return f});h(b,"masters/modules/wordcloud.src.js",[],function(){})});
//# sourceMappingURL=wordcloud.js.map