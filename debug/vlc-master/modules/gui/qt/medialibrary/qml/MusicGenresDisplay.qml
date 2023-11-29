/*****************************************************************************
 * Copyright (C) 2019 VLC authors and VideoLAN
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * ( at your option ) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA 02110-1301, USA.
 *****************************************************************************/
import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQml.Models 2.12
import org.videolan.vlc 0.1
import org.videolan.medialib 0.1

import "qrc:///util/" as Util
import "qrc:///widgets/" as Widgets
import "qrc:///style/"

Widgets.PageLoader {
    id: root

    pageModel: [{
        name: "all",
        default: true,
        component: genresComponent
    }, {
        name: "albums",
        component: albumGenreComponent
    }]

    Component {
        id: genresComponent
        /* List View */
        MusicGenres {
            onCurrentIndexChanged: History.viewProp.initialIndex = currentIndex

            searchPattern: MainCtx.search.pattern
            sortOrder: MainCtx.sort.order
            sortCriteria: MainCtx.sort.criteria

            onShowAlbumView: (id, name, reason) => {
                History.push([...root.pagePrefix, "albums"], { parentId: id, genreName: name }, reason)
            }
        }
    }

    Component {
        id: albumGenreComponent
        /* List View */
        MusicAlbums {
            id: albumsView

            property string genreName: ""

            gridViewMarginTop: 0

            header: Widgets.SubtitleLabel {
                text: I18n.qtr("Genres - %1").arg(genreName)
                leftPadding: albumsView.contentLeftMargin
                rightPadding: albumsView.contentRightMargin
                topPadding: VLCStyle.margin_large
                bottomPadding: VLCStyle.margin_normal
                width: root.width
                color: colorContext.fg.primary
            }

            searchPattern: MainCtx.search.pattern
            sortOrder: MainCtx.sort.order
            sortCriteria: MainCtx.sort.criteria

            onCurrentIndexChanged: History.viewProp.initialIndex = currentIndex
        }
    }
}
