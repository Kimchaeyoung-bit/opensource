﻿/*****************************************************************************
 * Copyright (C) 2020 VLC authors and VideoLAN
 *
 * Authors: Benjamin Arnaud <bunjee@omega.gg>
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
import QtQuick.Templates 2.12 as T
import QtQuick.Layouts 1.12

import org.videolan.medialib 0.1
import org.videolan.controls 0.1
import org.videolan.vlc 0.1

import "qrc:///widgets/" as Widgets
import "qrc:///style/"

T.ItemDelegate {
    id: root

    // Properties

    /* required */ property MLModel mlModel

    property bool isCurrent: false

    // Aliases
    // Private

    readonly property bool _isHover: contentItem.containsMouse || root.activeFocus

    // Signals

    signal itemClicked(var mouse)

    signal itemDoubleClicked(var mouse)

    // Settings

    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset,
                            implicitContentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset,
                             implicitContentHeight + topPadding + bottomPadding,
                             implicitIndicatorHeight + topPadding + bottomPadding)

    height: VLCStyle.play_cover_small + (VLCStyle.margin_xsmall * 2)

    verticalPadding: VLCStyle.margin_xsmall
    horizontalPadding: VLCStyle.margin_normal

    Accessible.onPressAction: root.itemClicked()

    // Childs

    readonly property ColorContext colorContext: ColorContext {
        id: theme
        colorSet: ColorContext.Item

        focused: root.activeFocus
        hovered: root.hovered
        enabled: root.enabled
    }

    background: Widgets.AnimatedBackground {
        active: visualFocus

        animate: theme.initialized
        backgroundColor: root.isCurrent ? theme.bg.highlight : theme.bg.primary
        activeBorderColor: theme.visualFocus

        Widgets.CurrentIndicator {
            length: parent.height - (margin * 2)

            margin: VLCStyle.dp(2, VLCStyle.scale)

            visible: isCurrent
        }
    }

    MouseArea {
        anchors.fill: parent

        drag.axis: Drag.XAndYAxis
        drag.smoothed: false

        drag.target: Widgets.DragItem {
            indexes: [index]

            onRequestData: {
                console.assert(indexes[0] === index)
                resolve([model])
            }

            onRequestInputItems: {
                const idList = data.map((o) => o.id)
                MediaLib.mlInputItem(idList, resolve)
            }
        }

        drag.onActiveChanged: {
            const dragItem = drag.target;

            if (drag.active == false)
                dragItem.Drag.drop();

            dragItem.Drag.active = drag.active;
        }

        onClicked: itemClicked(mouse)

        onDoubleClicked: itemDoubleClicked(mouse)
    }

    contentItem: RowLayout {
        spacing: VLCStyle.margin_xsmall

        RoundImage {
            implicitWidth: VLCStyle.play_cover_small
            implicitHeight: VLCStyle.play_cover_small
            Layout.fillHeight: true
            Layout.preferredWidth: height

            radius: width

            source: (model.cover) ? model.cover
                                  : VLCStyle.noArtArtistSmall

            Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter

            Rectangle {
                anchors.fill: parent

                radius: VLCStyle.play_cover_small

                color: "transparent"

                border.width: VLCStyle.dp(1, VLCStyle.scale)

                border.color: (isCurrent || _isHover) ? theme.accent
                                                      : theme.border
            }
        }

        Widgets.ScrollingText {
            label: artistName

            forceScroll: root.isCurrent || root._isHover
            clip: scrolling

            implicitHeight: artistName.implicitHeight
            implicitWidth: artistName.implicitWidth

            Layout.fillWidth: true
            Layout.fillHeight: true

            Widgets.ListLabel {
                id: artistName

                anchors {
                    verticalCenter: parent.verticalCenter
                }

                text: (model.name) ? model.name
                                   : I18n.qtr("Unknown artist")

                color: theme.fg.primary
            }
        }
    }
}
