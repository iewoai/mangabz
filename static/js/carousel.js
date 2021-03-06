; (function($) {
    var PicCarousel = (function() {
        function PicCarousel(element, options) {
            this.settings = $.extend(true, $.fn.PicCarousel.defaults, options || {});
            this.element = element;
            this.init();
        }
        PicCarousel.prototype = {
            init: function() {
                var me = this;
                me.poster = me.element;
                me.posterItemMain = me.poster.find("ul.poster-list");
                me.nextBtn = me.poster.find("div.poster-next-btn");
                me.prevBtn = me.poster.find("div.poster-prev-btn");
                me.nextBtnNew = $(".carousel-right-btn");
                me.prevBtnNew = $(".carousel-left-btn");
                me.posterItems = me.poster.find("li.poster-item");
                if (me.posterItems.size() % 2 == 0) {
                    me.posterItemMain.append(me.posterItems.ep(0).clone());
                    me.posterItems = me.posterItemMain.children;
                }
                me.posterFirstItem = me.posterItems.first();
                me.posterLastItem = me.posterItems.last();
                me.rotateFlag = true;
                me.setSettingValue();
                me.setPosterPost();
                me.nextBtn.click(function() {
                    if (me.rotateFlag) {
                        me.rotateFlag = false;
                        me.carouseRotate("left");
                    };
                });
                me.prevBtn.click(function() {
                    if (me.rotateFlag) {
                        me.rotateFlag = false;
                        me.carouseRotate("right");
                    };
                });
                me.nextBtnNew.click(function() {
                    if (me.rotateFlag) {
                        me.rotateFlag = false;
                        me.carouseRotate("left");
                    };
                });
                me.prevBtnNew.click(function() {
                    if (me.rotateFlag) {
                        me.rotateFlag = false;
                        me.carouseRotate("right");
                    };
                });

                if (me.settings.autoPlay) {
                    me.autoPlay();
                    me.poster.hover(function() {
                        window.clearInterval(me.timer);
                    },
                    function() {
                        me.autoPlay();
                    });
                }
            },
            autoPlay: function() {
                var me = this;
                me.timer = window.setInterval(function() {
                    me.nextBtn.click();
                },
                me.settings.delay);
            },
            carouseRotate: function(dir) {
                var me = this;
                var zIndexArr = [];
                if (dir === "left") {
                    me.posterItems.each(function() {
                        var self = $(this),
                        prev = self.prev().get(0) ? self.prev() : me.posterLastItem,
                        width = prev.width(),
                        height = prev.height(),
                        zIndex = prev.css("zIndex"),
                        opacity = prev.css("opacity"),
                        left = prev.css("left"),
                        top = prev.css("top");
                        zIndexArr.push(zIndex);
                        self.animate({
                            width: width,
                            height: height,
                            opacity: opacity,
                            left: left,
                            top: top
                        },
                        me.settings.speed,
                        function() {
                            me.rotateFlag = true;
                        });
                        if(width == 190){
                            $('.carousel-list-title').text(self.find('img').attr('data-title'));
                            $('.carousel-list-subtitle').text(self.find('img').attr('data-subtitle'));
                            $('.carousel-list-tag').html('<span>'+self.find('img').attr('data-tag').split(',').join('</span><span>')+'</span><a href="'+self.find('img').attr('data-url')+'" target="_blank" class="carousel-list-tag-start">开始阅读</a>');
                            $('.carousel-list-content').text(self.find('img').attr('data-content'));
                            carouselId = self.find('img').attr('data-id');
                        }
                    });
                    me.posterItems.each(function(i) {
                        $(this).css("zIndex", zIndexArr[i]);
                    })
                } else if (dir === "right") {
                    me.posterItems.each(function() {
                        var self = $(this),
                        next = self.next().get(0) ? self.next() : me.posterFirstItem,
                        width = next.width(),
                        height = next.height(),
                        zIndex = next.css("zIndex"),
                        opacity = next.css("opacity"),
                        left = next.css("left"),
                        top = next.css("top");
                        zIndexArr.push(zIndex);
                        self.animate({
                            width: width,
                            height: height,
                            opacity: opacity,
                            left: left,
                            top: top
                        },
                        me.settings.speed,
                        function() {
                            me.rotateFlag = true;
                        });
                        if(width == 190){
                            $('.carousel-list-title').text(self.find('img').attr('data-title'));
                            $('.carousel-list-subtitle').text(self.find('img').attr('data-subtitle'));
                            $('.carousel-list-tag').html('<span>'+self.find('img').attr('data-tag').split(',').join('</span><span>')+'</span><a href="'+self.find('img').attr('data-url')+'" target="_blank" class="carousel-list-tag-start">开始阅读</a>');
                            $('.carousel-list-content').text(self.find('img').attr('data-content'));
                            carouselId = self.find('img').attr('data-id');
                        }
                    });
                    me.posterItems.each(function(i) {
                        $(this).css("zIndex", zIndexArr[i]);
                    })
                }
            },
            setPosterPost: function() {
                var me = this;
                var sliceItems = me.posterItems.slice(1),
                sliceSize = sliceItems.size() / 2,
                rightSlice = sliceItems.slice(0, sliceSize),
                level = Math.floor(me.posterItems.size() / 2),
                leftSlice = sliceItems.slice(sliceSize);
                var rw = me.settings.posterWidth,
                rh = me.settings.posterHeight,
                gap = ((me.settings.width - me.settings.posterWidth) / 2) / level;
                var firstLeft = (me.settings.width - me.settings.posterWidth) / 2;
                var fixOffsetLeft = firstLeft + rw;
                rightSlice.each(function(i) {
                    level--;
                    rw = rw * me.settings.scale;
                    rh = rh * me.settings.scale;
                    var j = i;
                    $(this).css({
                        zIndex: level,
                        width: rw,
                        height: rh,
                        opacity: 1 / (++j),
                        left: fixOffsetLeft + (++i) * gap - rw,
                        top: me.setVertucalAlign(rh)
                    });
                });
                var lw = rightSlice.last().width(),
                lh = rightSlice.last().height(),
                oloop = Math.floor(me.posterItems.size() / 2);
                leftSlice.each(function(i) {
                    $(this).css({
                        zIndex: i,
                        width: lw,
                        height: lh,
                        opacity: 1 / oloop,
                        left: i * gap,
                        top: me.setVertucalAlign(lh)
                    });
                    lw = lw / me.settings.scale;
                    lh = lh / me.settings.scale;
                    oloop--;
                });
            },
            setVertucalAlign: function(height) {
                var me = this;
                var verticalType = me.settings.verticalAlign,
                top = 0;
                if (verticalType === "middle") {
                    top = (me.settings.height - height) / 2;
                } else if (verticalType === "top") {
                    top = 0;
                } else if (verticalType === "bottom") {
                    top = me.settings.height - height;
                } else {
                    top = (me.settings.height - height) / 2;
                };
                return top;
            },
            setSettingValue: function() {
                var me = this;
                me.poster.css({
                    width: me.settings.width,
                    height: me.settings.height
                });
                me.posterItemMain.css({
                    width: me.settings.width,
                    height: me.settings.height
                });
                var w = (me.settings.width - me.settings.posterWidth) / 2;
                me.nextBtn.css({
                    width: w,
                    height: me.settings.height,
                    zIndex: Math.ceil(me.posterItems.size() / 2)
                });
                me.prevBtn.css({
                    width: w,
                    height: me.settings.height,
                    zIndex: Math.ceil(me.posterItems.size() / 2)
                });
                me.posterFirstItem.css({
                    width: me.settings.posterWidth,
                    height: me.settings.posterHeight,
                    top: me.setVertucalAlign(me.settings.posterHeight),
                    left: w,
                    zIndex: Math.floor(me.posterItems.size() / 2)
                });
            }
        };
        return PicCarousel;
    })();
    $.fn.PicCarousel = function(options) {
        return this.each(function() {
            var me = $(this),
            instance = me.data("PicCarousel");
            if (!instance) {
                instance = new PicCarousel(me, options);
                me.data("PicCarousel", instance);
            }
        });
    };
    $.fn.PicCarousel.defaults = {
        "width": 1000,
        "height": 300,
        "posterWidth": 520,
        "posterHeight": 300,
        "scale": 0.9,
        "speed": 300,
        "autoPlay": false,
        "delay": 500,
        "verticalAlign": "middle"
    }
} (jQuery));