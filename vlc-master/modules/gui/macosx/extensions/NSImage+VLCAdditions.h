/*****************************************************************************
 * NSImage+VLCAdditions.h: MacOS X interface module
 *****************************************************************************
 * Copyright (C) 2023 VLC authors and VideoLAN
 *
 * Authors: Claudio Cambra <developer@claudiocambra.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA 02110-1301, USA.
 *****************************************************************************/

#import <Cocoa/Cocoa.h>

NS_ASSUME_NONNULL_BEGIN

@interface NSImage (VLCAdditions)

+ (instancetype)quickLookPreviewForLocalPath:(NSString*)path withSize:(NSSize)size;
+ (instancetype)quickLookPreviewForLocalURL:(NSURL*)url withSize:(NSSize)size;
+ (instancetype)compositeImageWithImages:(NSArray<NSImage *> * const)images
                                  frames:(NSArray<NSValue *> * const)frames
                                    size:(const NSSize)size;
+ (NSArray<NSValue *> *)framesForCompositeImageSquareGridWithImages:(NSArray<NSImage *> * const)images
                                                               size:(const NSSize)size
                                                      gridItemCount:(const NSUInteger)gridItemCount;

- (instancetype)imageTintedWithColor:(NSColor *)color;

@end

NS_ASSUME_NONNULL_END
