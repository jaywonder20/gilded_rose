# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name.startswith("Conjured"):
                GildedRose.conjured(item)

            elif item.name == "Aged Brie":

                GildedRose.aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                GildedRose.back_stage_access(item)
            else:

                GildedRose.regular_item(item)

    # Helper functions to handle different cases
    def aged_brie(self):
        """ 
         Aged Brie" actually increases in Quality the older it gets
        """
        if self.quality < 50:  # check to prevent quality exceeding maximum possible value of 50
            self.quality += 1
        self.sell_in -= 1

    def back_stage_access(self):
        """    
        increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        Quality drops to 0 after the concert"""
        if 10 >= self.sell_in > 5:
            self.quality += 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in -= 1

    def regular_item(self):
        """" 
         For regular items At the end of each day the  system lowers both values for every item
        """
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality -= 2
            else:
                self.quality = self.quality - 1
        self.sell_in -= 1

    def conjured(self):
        """ Conjured items degrade in Quality twice as fast as normal items"""
        self.quality = (self.quality - 2) if self.quality > 2 else 0
        self.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
